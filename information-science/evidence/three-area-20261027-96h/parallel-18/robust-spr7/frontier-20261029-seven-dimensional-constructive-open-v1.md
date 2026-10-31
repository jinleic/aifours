# Sharpness of the six-dimensional span obstruction

**Status: WRITTEN-checked-in-kernel; author candidate, not parent adoption.** For every box in the explicit 14-dimensional neighborhood of `frontier-20261029-six-dimensional-endpoint-derivatives-open-obstruction-v1.md`, no common numerator belongs to the real span of the four parity endpoints and the first **two** midpoint derivatives, but a common numerator does belong to the corresponding span with the **third** midpoint derivative added. Thus the particular six-dimensional obstruction cannot be extended mechanically to this seven-dimensional space.

## Anchor numerator in the seven-generator span

For the anchor box, let \(g_0,\ldots,g_3\) be its four parity endpoint generators and \(m\) its midpoint. With
\[
(c_0,\ldots,c_6)=\left(
\frac{10522347564561666580543283}{98690440179273240906300},
\frac{10650458546169421414083283}{98690440179273240906300},
-\frac{974592115411710414229}{1023826002264250203942},
\frac{1998418117675960618171}{1023826002264250203942},
\frac{27110296148461976}{213853048267285},1,
-\frac{11252750427857639}{1796365605445194}\right),
\]
set
\[
b=\sum_{j=0}^3c_jg_j+c_4Dm+c_5D^2m+c_6D^3m.
\]
Its exact ascending monomial coefficients are
\[
\left(\frac{1097493681927330602528436}{140647942049669335225},
\frac{13809302260586664639419}{2559820987759401450},
\frac{9821258250411126299731201}{421943826149008005675},
\frac{8762326327973848034899}{1706547325172934300},
\frac{484139679169480260819881}{44415139594632421650},
\frac{4501088371387216578827}{5119641975518802900},
\frac{134858348057668071804809}{120555378899716573050},1\right).
\]
The independent replay verified exact generator reconstruction and 256 strict compactified Bernstein coefficients across the four actual corners, with margin
\[
\delta_7=\frac{940561989047572415961248490663441143236147}
{9316837260019698480362469636893864204697600000}>0.
\]
The six-dimensional obstruction packet separately verifies the anchor's 28 strict corner Hurwitz minors. Kharitonov and affine minimization show this \(b\) is common SPR for the full anchor box.

## The moving span remains sufficient nearby

Perturb every endpoint by at most \(\varepsilon=10^{-92}\), and form its **new** endpoint generators and midpoint derivatives. Keep the seven displayed scalar coefficients \(c_j\) fixed, defining the moving polynomial \(b'\) in that perturbed box's own seven-generator span. The monic leading coefficient remains positive because the two odd generators have fixed monic degree-seven leading coefficients and all added derivatives have degree at most six.

Each generator coefficient moves by at most \(J_j\varepsilon\), where
\[
(J_0,\ldots,J_6)=(1,1,1,1,7,42,210).
\]
Writing \(C=\sum|c_j|J_j\), the independent replay verifies \(|b'_j-b_j|\le C\varepsilon\), the bound
\[
L=7\sum_j|b_j|+8\left(1+\sum_j u_j+7\right)C
=\frac{29734963103112405882395650873723987}{6692502693140372999399625000},
\]
and \(2\varepsilon L<\delta_7\). For a perturbed denominator \(a'\), choose an anchor \(a\) within \(\varepsilon\) coefficientwise. Monomial expansion gives
\[
\frac{|P_{a',b'}(t)-P_{a,b}(t)|}{(1+t)^7}\le\varepsilon L<\delta_7/2.
\]
Thus \(b'\) is common SPR on the entire perturbed box; stability and the six-generator no-go there are already proved by the cited open theorem. This is a continuous constructive family, not a claim that a single fixed polynomial belongs to all moving spans.

Anchor seven-generator coefficients, numerator and leaves: `frontier-20261029-seven-dimensional-constructive-separator-frozen-v1.json`, SHA-256 `20bd10e2128df44cab2575d1e7eea098baf612c4d134f80e1f324cb039a6a054`. Open bounds: `frontier-20261029-seven-dimensional-constructive-open-frozen-v1.json`, SHA-256 `88e4dd24c4dafa0beb6a3885c1854bbb1bb015bc1c180127bcf8477a9d49ca8d`. Independent checker `frontier-20261029-seven-dimensional-constructive-open-independent-kernel-v1.py`, SHA-256 `6329a339f4ade28782419e33827de1431a2cf1929f5226f09f950f4504973910`; receipt `frontier-20261029-seven-dimensional-constructive-open-independent-result-v1.json`, SHA-256 `73dd0264e5d61454ce725a0f91b24e240a495d087da5266694e47c458dd2af0d`.

The finite calculations use exact integers and `fractions.Fraction` on one Python Eval host; stability, affine minimization and perturbation estimates are written deductions. No formal proof, cross-vendor review, novelty clearance, or arbitrary-box verdict is claimed.
