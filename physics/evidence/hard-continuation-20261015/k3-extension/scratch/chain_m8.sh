set -e
cd /Users/jinleic/repos/aifours/physics/evidence/hard-continuation-20261015/k3-extension
prev=scratch/init_k3_m8_T128.json
a=4.2669728888708
for T in 256 512 1024; do
  python3 code/explore_search.py --k 3 --T $T --alpha $a --rounds 4 --iters 300 --init $prev --out scratch/opt_k3_m8_T$T.json > scratch/opt_k3_m8_T$T.log 2>&1
  a=$(python3 -c "import json;print(json.load(open('scratch/opt_k3_m8_T'+'$T'+'.json'))['final_alpha'])")
  prev=scratch/opt_k3_m8_T$T.json
done
echo chain-done
