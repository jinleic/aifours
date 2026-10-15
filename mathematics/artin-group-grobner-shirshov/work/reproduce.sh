#!/bin/sh
# Regenerate every computational artifact in evidence/ (python3 >= 3.10, stdlib only).
# Run from the target directory:  sh work/reproduce.sh      (about 6 minutes, 1 core)
set -e
cd "$(dirname "$0")/.."
export PYTHONDONTWRITEBYTECODE=1
mkdir -p evidence/oracle evidence/classify evidence/certify evidence/kb

# 0. oracle self-tests (relation invariance, Delta twist, inverses are exercised in certify)
python3 work/test_oracle.py > evidence/test_oracle.txt
# 0b. exact integer validation of the numerically generated Coxeter tables
python3 work/validate_tables.py > evidence/validate_tables.json

# 1. reduced GS basis from the Garside normal-form oracle (positive part, leading words <= 15)
for spec in "A 3 0,2,1" "B 3 0,2,1" "B 3 0,1,2" "H 3 0,2,1" "H 3 2,1,0"; do
  set -- $spec; o=$(echo $3 | tr -d ,)
  python3 work/gs_oracle.py $1 $2 15 --positive --order $3 > evidence/oracle/pos_$1$2_o${o}_L15.jsonl
done

# 2. exact growth classification of the reduced basis (Theorem B automaton + SCC criterion)
(for t in "A 3" "B 3" "H 3" "A 4" "B 4" "D 4" "F 4"; do python3 work/classify.py $t --all-orders; done
 python3 work/classify.py I 0 --m 3 --all-orders; python3 work/classify.py I 0 --m 6 --all-orders) \
  > evidence/classify/group_positive.jsonl
python3 work/classify.py H 4 --all-orders > evidence/classify/group_positive_H4.jsonl
(for t in "A 3" "B 3" "H 3" "A 4" "B 4" "D 4" "F 4" "H 4"; do python3 work/classify.py $t --all-orders --monoid; done
 python3 work/classify.py I 0 --m 3 --all-orders --monoid; python3 work/classify.py I 0 --m 6 --all-orders --monoid) \
  > evidence/classify/monoid.jsonl

# 3. certificates: Theorem E (B3), Theorem C (dihedral m = 3..12), Theorem F (D4)
python3 work/certify.py B3 --Lmax 14 > evidence/certify/B3.json
python3 work/derivations.py B3 > evidence/certify/B3_derivations.txt
for m in 3 4 5 6 7 8 9 10 11 12; do python3 work/certify.py I2_$m --Lmax 12 > evidence/certify/I2_$m.json; done
python3 work/extract_families.py B 3 --order 0,2,1 > work/specs_B3auto.json
python3 work/certify.py B3auto --Lmax 12 > evidence/certify/B3auto.json
python3 work/extract_families.py D 4 --order 0,2,3,1 > work/specs_D4.json
python3 work/certify.py D4 --Lmax 10 > evidence/certify/D4.json
python3 work/extract_families.py H 3 --order 2,0,1 > work/specs_H3.json
python3 work/extract_families.py H 3 --order 0,2,1 > work/specs_H3b.json
python3 work/extract_families.py A 3 --order 0,2,1 > work/specs_A3.json
for s in H3 H3b A3; do python3 work/certify.py $s --Lmax 12 > evidence/certify/$s.json; done
# 4. independent Knuth-Bendix completion vs oracle / spec
(python3 work/kb_compare.py B 3 --order 0,2,1 --maxlen 16 --L 14 --spec B3
 python3 work/kb_compare.py I 0 --m 6 --maxlen 16 --L 14 --spec I2_6
 python3 work/kb_compare.py I 0 --m 5 --maxlen 16 --L 14 --spec I2_5
 python3 work/kb_compare.py A 3 --order 0,1,2 --maxlen 14 --L 12
 python3 work/kb_compare.py B 3 --order 0,1,2 --maxlen 14 --L 12
 python3 work/kb_compare.py B 3 --order 0,2,1 --maxlen 15 --L 15 --monoid
 python3 work/kb_compare.py D 4 --order 0,2,3,1 --maxlen 12 --L 10 --spec D4) > evidence/kb/kb_compare.jsonl
for s in D4 B3auto H3 H3b A3; do python3 work/render_families.py work/specs_$s.json > evidence/certify/${s}_families.md; done

# 5. the published B3 monoid basis (Iqbal-Munir-Ayub-Nizami 2024)
python3 work/check_iqbal2024.py 13 > evidence/iqbal2024_check_L13_as_printed.json
python3 work/check_iqbal2024.py 13 --corrected > evidence/iqbal2024_check_L13_corrected.json
python3 work/certify_iqbal2024.py > evidence/certify/iqbal2024_corrected_certificate.json

# 6. explicit paired regular-expression GS bases (Theorem G; generally non-reduced)
for spec in "B4 B 4 0,2,3,1" "F4 F 4 0,2,3,1" "A4 A 4 0,2,3,1" "B5 B 5 0,2,4,1,3"; do
  set -- $spec
  python3 work/complement_rules.py "$2" "$3" --order "$4" > "evidence/certify/${1}_paired_rules.json"
  python3 work/render_complement_rules.py "evidence/certify/${1}_paired_rules.json" > "evidence/certify/${1}_paired_expression.txt"
  python3 work/check_complement_rules.py "evidence/certify/${1}_paired_rules.json" > "evidence/certify/${1}_paired_certificate.json"
done
for name in B4 F4; do
  python3 work/check_complement_compositions.py "evidence/certify/${name}_paired_rules.json" > "evidence/certify/${name}_composition_checks.json"
done
python3 work/check_signed_b.py > evidence/certify/signed_b_formula.json
echo done
