import FWCore.ParameterSet.Config as cms
import os
def customise(process):

  slhacontent = """# NMSSMTools OUTPUT IN SLHA FORMAT
# Info about spectrum calculator
BLOCK SPINFO   # Program information
     1   NMSSMTools # Spectrum calculator
     2   3.2.0      # Version number
     8   1          # Higgs mass precision
     3   # Muon magn. mom. more than 2 sigma away
# Input parameters
BLOCK MODSEL
    3     1         # NMSSM PARTICLE CONTENT
BLOCK SMINPUTS
     1     1.27920000E+02   # ALPHA_EM^-1(MZ)
     2     1.16639000E-05   # GF
     3     1.17200000E-01   # ALPHA_S(MZ)
     4     9.11870000E+01   # MZ
     5     4.20000000E+00   # MB(MB)
     6     1.73300000E+02   # MTOP (POLE MASS)
     7     1.77700000E+00   # MTAU
# SMINPUTS Beyond SLHA:
# MW:     0.80420000E+02
# MS:     0.19000000E+00
# MC:     0.14000000E+01
# VUS:     0.22000000E+00
# VCB:     0.40000000E-01
# VUB:     0.40000000E-02
BLOCK MINPAR
     3     2.60000000E+00   # TANBETA(MZ)
BLOCK EXTPAR
     1     3.00000000E+02   # M1
     2     6.00000000E+02   # M2
     3     1.00000000E+03   # M3
    11     1.13320950E+03   # ATOP
    12     1.13320950E+03   # ABOTTOM
    13     1.13320950E+03   # ATAU
    16     1.13320950E+03   # AMUON
    31     1.00000000E+03   # LEFT SELECTRON
    32     1.00000000E+03   # LEFT SMUON
    33     1.00000000E+03   # LEFT STAU
    34     1.00000000E+03   # RIGHT SELECTRON
    35     1.00000000E+03   # RIGHT SMUON
    36     1.00000000E+03   # RIGHT STAU
    41     1.00000000E+03   # LEFT 1ST GEN. SQUARKS
    42     1.00000000E+03   # LEFT 2ND GEN. SQUARKS
    43     1.00000000E+03   # LEFT 3RD GEN. SQUARKS
    44     1.00000000E+03   # RIGHT U-SQUARKS
    45     1.00000000E+03   # RIGHT C-SQUARKS
    46     1.00000000E+03   # RIGHT T-SQUARKS
    47     1.00000000E+03   # RIGHT D-SQUARKS
    48     1.00000000E+03   # RIGHT S-SQUARKS
    49     1.00000000E+03   # RIGHT B-SQUARKS
    61     6.00000000E-01   # LAMBDA
    62     1.20000000E-01   # KAPPA
    63    -5.10000000E+02   # ALAMBDA
    64     3.76318330E+01   # AKAPPA
    65    -2.00000000E+02   # MUEFF
# 
BLOCK MASS   # Mass spectrum 
#  PDG Code     mass             particle 
        25     9.50000000E+01   # lightest neutral scalar
        35     1.25300000E+02   # second neutral scalar
        45     5.76818257E+02   # third neutral scalar
        36     1.09274397E+02   # lightest pseudoscalar
        46     5.76839702E+02   # second pseudoscalar
        37     5.65627658E+02   # charged Higgs
   1000001     1.03816356E+03   #  ~d_L
   2000001     1.03719659E+03   #  ~d_R
   1000002     1.03601090E+03   #  ~u_L
   2000002     1.03654529E+03   #  ~u_R
   1000003     1.03816356E+03   #  ~s_L
   2000003     1.03719659E+03   #  ~s_R
   1000004     1.03601090E+03   #  ~c_L
   2000004     1.03654529E+03   #  ~c_R
   1000005     1.03578175E+03   #  ~b_1
   2000005     1.03957830E+03   #  ~b_2
   1000006     9.61798112E+02   #  ~t_1
   2000006     1.12575819E+03   #  ~t_2
   1000011     1.00077837E+03   #  ~e_L
   2000011     1.00067504E+03   #  ~e_R
   1000012     9.98544999E+02   #  ~nue_L
   1000013     1.00077837E+03   #  ~mu_L
   2000013     1.00067504E+03   #  ~mu_R
   1000014     9.98544999E+02   #  ~numu_L
   1000015     9.99262886E+02   #  ~tau_1
   2000015     1.00219154E+03   #  ~tau_2
   1000016     9.98544999E+02   #  ~nutau_L
   1000021     1.07903269E+03   #  ~g
   1000022    -9.78138073E+01   # neutralino(1)
   1000023    -2.27083370E+02   # neutralino(2)
   1000025     2.27948047E+02   # neutralino(3)
   1000035     3.03709218E+02   # neutralino(4)
   1000045     6.21809001E+02   # neutralino(5)
   1000024    -2.07786084E+02   # chargino(1)
   1000037     6.21777058E+02   # chargino(2)
# 
# Low energy observables
BLOCK LOWEN
# Exp. 2 Sigma: 3.03E-04 < BR(b -> s gamma) < 4.01E-04:
     1     3.63828634E-04   # BR(b -> s gamma)
    11     4.02169521E-04   # (BR(b -> s gamma)+Theor.Err.)
    12     3.05817682E-04   # (BR(b -> s gamma)-Theor.Err.)
# Exp. 2 Sigma: 4.99E-01 < Delta M_d < 5.15E-01:
     2     6.23706692E-01   # Delta M_d in ps^-1
    21     1.08922721E+00   # Delta M_d +Theor.Err.
    22     1.67316904E-01   # Delta M_d -Theor.Err.
# Exp. 2 Sigma: 1.753E+01 < Delta Ms < 1.801E+01:
     3     2.16085611E+01   # Delta M_s in ps^-1
    31     2.85155787E+01   # Delta M_s +Theor.Err.
    32     1.48345561E+01   # Delta M_s -Theor.Err.
# Exp. 95% C.L.: BR(Bs->mu+mu-) < 4.5E-09:
     4     3.66089417E-09   # BR(Bs -> mu+mu-)
    41     6.21795983E-09   # BR(Bs -> mu+mu-)+Theor.Err.
    42     1.77711962E-09   # BR(Bs -> mu+mu-)-Theor.Err.
# Exp. 2 Sigma: 8.90E-05 < BR(B+ > tau+ + nu_tau) < 2.45E-04:
     5     1.31637772E-04   # BR(B+ -> tau+ + nu_tau)
    51     2.63327035E-04   # BR(B+ -> tau+ + nu_tau) + Theor.Err.
    52     5.68117034E-05   # BR(B+ -> tau+ + nu_tau) - Theor.Err.
# BSM contr. to the muon anomalous magn. moment:
     6    -8.34134468E-11   # Del_a_mu
    61     1.99269778E-10   # Del_a_mu + Theor.Err.
    62    -3.66096671E-10   # Del_a_mu - Theor.Err.
# Minimal Exp.-SM (2 sigma):  8.77306222E-10
# Maximal Exp.-SM (2 sigma):  4.61144414E-09
# 
BLOCK HMIX Q=  1.00000000E+03 # (STOP/SBOTTOM MASSES)
     1    -2.00000000E+02   # MUEFF
     2     2.57525562E+00   # TAN(BETA)
     3     2.41822895E+02   # V(Q)
     4     3.25992325E+05   # MA^2
     5     1.64144636E+04   # MP^2
# 
# 3*3 Higgs mixing
BLOCK NMHMIX
  1  1    -9.14795786E-02   # S_(1,1)
  1  2     1.47091996E-01   # S_(1,2)
  1  3     9.84883461E-01   # S_(1,3)
  2  1     3.77479953E-01   # S_(2,1)
  2  2     9.20339630E-01   # S_(2,2)
  2  3    -1.02390679E-01   # S_(2,3)
  3  1     9.21488129E-01   # S_(3,1)
  3  2    -3.62407107E-01   # S_(3,2)
  3  3     1.39716561E-01   # S_(3,3)
# 
# 3*3 Pseudoscalar Higgs mixing
BLOCK NMAMIX
  1  1     1.29576774E-01   # P_(1,1)
  1  2     4.98372206E-02   # P_(1,2)
  1  3     9.90315950E-01   # P_(1,3)
  2  1     9.24302659E-01   # P_(2,1)
  2  2     3.55501023E-01   # P_(2,2)
  2  3    -1.38831980E-01   # P_(2,3)
# 
# 3rd generation sfermion mixing
BLOCK STOPMIX  # Stop mixing matrix
  1  1    -7.08196418E-01   # Rst_(1,1)
  1  2     7.06015462E-01   # Rst_(1,2)
  2  1    -7.06015462E-01   # Rst_(2,1)
  2  2    -7.08196418E-01   # Rst_(2,2)
BLOCK SBOTMIX  # Sbottom mixing matrix
  1  1    -6.14932387E-01   # Rsb_(1,1)
  1  2     7.88579837E-01   # Rsb_(1,2)
  2  1    -7.88579837E-01   # Rsb_(2,1)
  2  2    -6.14932387E-01   # Rsb_(2,2)
BLOCK STAUMIX  # Stau mixing matrix
  1  1    -6.94520358E-01   # Rsl_(1,1)
  1  2     7.19473052E-01   # Rsl_(1,2)
  2  1    -7.19473052E-01   # Rsl_(2,1)
  2  2    -6.94520358E-01   # Rsl_(2,2)
# 
# Gaugino-Higgsino mixing
BLOCK NMIX  # 5*5 Neutralino Mixing Matrix
  1  1    -4.40029145E-02   # N_(1,1)
  1  2     4.58056753E-02   # N_(1,2)
  1  3    -1.40922328E-02   # N_(1,3)
  1  4     4.28128247E-01   # N_(1,4)
  1  5     9.01372951E-01   # N_(1,5)
  2  1    -6.84791003E-02   # N_(2,1)
  2  2     8.00337876E-02   # N_(2,2)
  2  3    -7.08726134E-01   # N_(2,3)
  2  4     6.22764805E-01   # N_(2,4)
  2  5    -3.14287243E-01   # N_(2,5)
  3  1    -2.00332521E-01   # N_(3,1)
  3  2     6.77415257E-02   # N_(3,2)
  3  3     6.99124361E-01   # N_(3,3)
  3  4     6.16063116E-01   # N_(3,4)
  3  5    -2.94905632E-01   # N_(3,5)
  4  1     9.76225036E-01   # N_(4,1)
  4  2     3.68650304E-02   # N_(4,2)
  4  3     9.32201135E-02   # N_(4,3)
  4  4     1.87574227E-01   # N_(4,4)
  4  5    -4.18517399E-02   # N_(4,5)
  5  1    -1.50305121E-02   # N_(5,1)
  5  2     9.92747948E-01   # N_(5,2)
  5  3     6.61923090E-03   # N_(5,3)
  5  4    -1.18963645E-01   # N_(5,4)
  5  5     5.42516847E-03   # N_(5,5)
# 
BLOCK UMIX  # Chargino U Mixing Matrix
  1  1     9.83153370E-03   # U_(1,1)
  1  2    -9.99951669E-01   # U_(1,2)
  2  1     9.99951669E-01   # U_(2,1)
  2  2     9.83153370E-03   # U_(2,2)
# 
BLOCK VMIX  # Chargino V Mixing Matrix
  1  1     1.67489961E-01   # V_(1,1)
  1  2    -9.85873781E-01   # V_(1,2)
  2  1     9.85873781E-01   # V_(2,1)
  2  2     1.67489961E-01   # V_(2,2)
# 
# Higgs reduced couplings
# (as compared to a SM Higgs with same mass)
BLOCK REDCOUP
# H1
  1  1     1.57596495E-01   # U-type fermions
  1  2    -2.54832618E-01   # D-type fermions
  1  3     1.04448414E-01   # W,Z bosons
  1  4     1.97609448E-01   # Gluons
  1  5     2.00845695E-01   # Photons
# H2
  2  1     9.86065208E-01   # U-type fermions
  2  2     1.05153747E+00   # D-type fermions
  2  3     9.94502356E-01   # W,Z bosons
  2  4     9.86291814E-01   # Gluons
  2  5     9.70966354E-01   # Photons
# H3
  3  1    -3.88288223E-01   # U-type fermions
  3  2     2.56696889E+00   # D-type fermions
  3  3    -7.45612049E-03   # W,Z bosons
  3  4     3.90406457E-01   # Gluons
  3  5     1.63344971E+00   # Photons
# A1
  4  1     5.33963199E-02   # U-type fermions
  4  2     3.60959123E-01   # D-type fermions
  4  3     0.00000000E+00   # W,Z bosons
  4  4     4.61584381E-02   # Gluons
  4  5     3.42770878E-01   # Photons
# A2
  5  1     3.80888944E-01   # U-type fermions
  5  2     2.57480926E+00   # D-type fermions
  5  3     0.00000000E+00   # W,Z bosons
  5  4     3.84665898E-01   # Gluons
  5  5     3.63492799E-01   # Photons
# 
# GAUGE AND YUKAWA COUPLINGS AT THE SUSY SCALE
BLOCK GAUGE Q=  1.00000000E+03 # (SUSY SCALE)
     1     3.62459603E-01   # g1(Q,DR_bar)
     2     6.42566822E-01   # g2(Q,DR_bar)
     3     1.05976273E+00   # g3(Q,DR_bar)
BLOCK YU Q=  1.00000000E+03 # (SUSY SCALE)
  3  3     9.25551241E-01   # HTOP(Q,DR_bar)
BLOCK YD Q=  1.00000000E+03 # (SUSY SCALE)
  3  3     3.93485317E-02   # HBOT(Q,DR_bar)
BLOCK YE Q=  1.00000000E+03 # (SUSY SCALE)
  3  3     2.78125730E-02   # HTAU(Q,DR_bar)
# 
# SOFT TRILINEAR COUPLINGS AT THE SUSY SCALE
BLOCK AU Q=  1.00000000E+03 # (SUSY SCALE)
  3  3     1.13320950E+03   # ATOP
BLOCK AD Q=  1.00000000E+03 # (SUSY SCALE)
  3  3     1.13320950E+03   # ABOT
BLOCK AE Q=  1.00000000E+03 # (SUSY SCALE)
  2  2     1.13320950E+03   # AMUON
  3  3     1.13320950E+03   # ATAU
# 
# SOFT MASSES AT THE SUSY SCALE
BLOCK MSOFT Q=  1.00000000E+03 # (SUSY SCALE)
     1     3.00000000E+02   # M1
     2     6.00000000E+02   # M2
     3     1.00000000E+03   # M3
    21     2.36942523E+05   # M_HD^2
    22     2.69359291E+04   # M_HU^2
    31     1.00000000E+03   # M_eL
    32     1.00000000E+03   # M_muL
    33     1.00000000E+03   # M_tauL
    34     1.00000000E+03   # M_eR
    35     1.00000000E+03   # M_muR
    36     1.00000000E+03   # M_tauR
    41     1.00000000E+03   # M_q1L
    42     1.00000000E+03   # M_q2L
    43     1.00000000E+03   # M_q3L
    44     1.00000000E+03   # M_uR
    45     1.00000000E+03   # M_cR
    46     1.00000000E+03   # M_tR
    47     1.00000000E+03   # M_dR
    48     1.00000000E+03   # M_sR
    49     1.00000000E+03   # M_bR
# 
# NMSSM SPECIFIC PARAMETERS THE SUSY SCALE
BLOCK NMSSMRUN Q=  1.00000000E+03 # (SUSY SCALE)
     1     6.00000000E-01   # LAMBDA(Q,DR_bar)
     2     1.20000000E-01   # KAPPA(Q,DR_bar)
     3    -5.10000000E+02   # ALAMBDA
     4     3.76318330E+01   # AKAPPA
     5    -2.00000000E+02   # MUEFF
    10    -1.74825034E+03   # MS^2
# 
# GAUGE AND YUKAWA COUPLINGS AT THE GUT SCALE
BLOCK GAUGE Q=  1.96152992E+16 # (GUT SCALE)
     1     7.11402404E-01   # g1(MGUT,DR_bar), GUT normalization
     2     7.11402404E-01   # g2(MGUT,DR_bar)
     3     7.02978760E-01   # g3(MGUT,DR_bar)
BLOCK YU Q=  1.96152992E+16 # (GUT SCALE)
  3  3     8.29138649E-01   # HTOP(MGUT,DR_bar)
BLOCK YD Q=  1.96152992E+16 # (GUT SCALE)
  3  3     1.80984612E-02   # HBOT(MGUT,DR_bar)
BLOCK YE Q=  1.96152992E+16 # (GUT SCALE)
  3  3     2.17551428E-02   # HTAU(MGUT,DR_bar)
# 
# SOFT TRILINEAR COUPLINGS AT THE GUT SCALE
BLOCK AU Q=  1.96152992E+16 # (GUT SCALE)
  3  3     1.02128593E+04   # ATOP
BLOCK AD Q=  1.96152992E+16 # (GUT SCALE)
  3  3     4.15720481E+03   # ABOT
BLOCK AE Q=  1.96152992E+16 # (GUT SCALE)
  2  2     2.02868102E+03   # AMUON
  3  3     2.05446528E+03   # ATAU
# 
# SOFT MASSES SQUARED AT THE GUT SCALE
BLOCK MSOFT Q=  1.96152992E+16 # (GUT SCALE)
     1     7.30350203E+02   # M1
     2     7.87220985E+02   # M2
     3     4.67792576E+02   # M3
    21     5.36515429E+06   # M_HD^2
    22     4.07671758E+07   # M_HU^2
    31     7.64360002E+05   # M_eL^2
    32     7.64360002E+05   # M_muL^2
    33     7.65425928E+05   # M_tauL^2
    34     9.24038941E+05   # M_eR^2
    35     9.24038941E+05   # M_muR^2
    36     9.26179134E+05   # M_tauR^2
    41     5.32654238E+04   # M_q1L^2
    42     5.32654238E+04   # M_q2L^2
    43     1.11491014E+07   # M_q3L^2
    44     2.54211928E+05   # M_uR^2
    45     2.54211928E+05   # M_cR^2
    46     2.29096793E+07   # M_tR^2
    47     2.56771869E+05   # M_dR^2
    48     2.56771869E+05   # M_sR^2
    49     2.61151115E+05   # M_bR^2
# 
# NMSSM SPECIFIC PARAMETERS AT THE GUT SCALE
BLOCK NMSSMRUN Q=  1.96152992E+16 # (GUT SCALE)
     1     1.14613203E+00   # LAMBDA(MGUT,DR_bar)
     2     2.70925785E-01   # KAPPA(MGUT,DR_bar)
     3     5.30652296E+03   # ALAMBDA
     4     2.71316330E+03   # AKAPPA
    10     1.12530733E+07   # MS^2
# 
# FINE-TUNING parameter d(ln Mz^2)/d(ln PS^2)
         1     3.24589721E+00   # PS=MHU
         2     4.22880124E+00   # PS=MHD
         3     4.29521658E-03   # PS=MS
         4    -4.71875622E+00   # PS=ALAMBDA
         5     1.84912731E-03   # PS=AKAPPA
         6    -0.00000000E+00   # PS=XIF
         7     0.00000000E+00   # PS=XIS
         8     0.00000000E+00   # PS=MUP
         9    -0.00000000E+00   # PS=MSP
        10    -0.00000000E+00   # PS=M3H
        11     7.16942678E-01   # PS=LAMBDA
        12    -3.75205893E-01   # PS=KAPPA
        13     6.82926403E-01   # PS=HTOP
        14    -6.83199986E-01   # PS=G
        15     4.71875622E+00   # MAX
        16                  4   # IMAX
# 
# REDUCED CROSS SECTIONS AT LHC
        11     1.12768971E-02   # VBF -> H1 -> tautau
        12     6.78101954E-03   # ggF -> H1 -> ZZ
        13     6.78101954E-03   # ggF -> H1 -> WW
        14     2.50750443E-02   # ggF -> H1 -> gammagamma
        15     7.00535253E-03   # VBF -> H1 -> gammagamma
        21     1.02478115E+00   # VBF -> H2 -> tautau
        22     9.01555525E-01   # ggF -> H2 -> ZZ
        23     9.01555525E-01   # ggF -> H2 -> WW
        24     8.59438020E-01   # ggF -> H2 -> gammagamma
        25     8.73806633E-01   # VBF -> H2 -> gammagamma
        31     5.03879044E-03   # VBF -> H3 -> tautau
        32     1.16551823E-04   # ggF -> H3 -> ZZ
        33     1.16551823E-04   # ggF -> H3 -> WW
        34     5.59409867E+00   # ggF -> H3 -> gammagamma
        35     2.04043129E-03   # VBF -> H3 -> gammagamma
# HIGGS + TOP BRANCHING RATIOS IN SLHA FORMAT
# Info about decay package
BLOCK DCINFO   # Program information
     1   NMSSMTools # Decay package
     2   3.2.0      # Version number
#           PDG          Width
DECAY        25     1.47553643E-04   # Lightest neutral Higgs scalar
     2.62700783E-02    2          21        21   # BR(H_1 -> gluon gluon)
     3.06351927E-04    2          13       -13   # BR(H_1 -> muon muon)
     8.64699326E-02    2          15       -15   # BR(H_1 -> tau tau)
     6.53264728E-04    2           3        -3   # BR(H_1 -> s sbar)
     1.52190441E-02    2           4        -4   # BR(H_1 -> c cbar)
     8.69892373E-01    2           5        -5   # BR(H_1 -> b bbar)
     0.00000000E+00    2           6        -6   # BR(H_1 -> t tbar)
     2.78492159E-04    2          24       -24   # BR(H_1 -> W+ W-)
     1.76762136E-07    2          23        23   # BR(H_1 -> Z Z)
     9.09559795E-04    2          22        22   # BR(H_1 -> gamma gamma)
     7.26252043E-07    2          23        22   # BR(H_1 -> Z gamma)
DECAY        35     4.22871311E-03   # 2nd neutral Higgs scalar
     5.04184498E-02    2          21        21   # BR(H_2 -> gluon gluon)
     2.40065992E-04    2          13       -13   # BR(H_2 -> muon muon)
     6.78206323E-02    2          15       -15   # BR(H_2 -> tau tau)
     5.05087055E-04    2           3        -3   # BR(H_2 -> s sbar)
     2.68452654E-02    2           4        -4   # BR(H_2 -> c cbar)
     6.42471588E-01    2           5        -5   # BR(H_2 -> b bbar)
     0.00000000E+00    2           6        -6   # BR(H_2 -> t tbar)
     1.87465877E-01    2          24       -24   # BR(H_2 -> W+ W-)
     2.06320884E-02    2          23        23   # BR(H_2 -> Z Z)
     2.09660884E-03    2          22        22   # BR(H_2 -> gamma gamma)
     1.50433686E-03    2          23        22   # BR(H_2 -> Z gamma)
DECAY        45     7.40417525E+00   # 3rd neutral Higgs scalar
     6.96763845E-04    2          21        21   # BR(H_3 -> gluon gluon)
     3.76134846E-06    2          13       -13   # BR(H_3 -> muon muon)
     1.06383082E-03    2          15       -15   # BR(H_3 -> tau tau)
     5.92320509E-06    2           3        -3   # BR(H_3 -> s sbar)
     1.13527340E-04    2           4        -4   # BR(H_3 -> c cbar)
     7.82564985E-03    2           5        -5   # BR(H_3 -> b bbar)
     3.80772261E-01    2           6        -6   # BR(H_3 -> t tbar)
     4.20878462E-04    2          24       -24   # BR(H_3 -> W+ W-)
     2.03570883E-04    2          23        23   # BR(H_3 -> Z Z)
     3.03363892E-06    2          22        22   # BR(H_3 -> gamma gamma)
     7.90075198E-07    2          23        22   # BR(H_3 -> Z gamma)
     2.70511012E-02    2          25        25   # BR(H_3 -> H_1 H_1)
     1.24407613E-01    2          25        35   # BR(H_3 -> H_1 H_2)
     1.63432542E-03    2          35        35   # BR(H_3 -> H_2 H_2)
     1.37194121E-04    2          36        36   # BR(H_3 -> A_1 A_1)
     1.32318397E-01    2          23        36   # BR(H_3 -> A_1 Z)
     1.00603406E-01    2     1000022   1000022   # BR(H_3 -> neu_1 neu_1)
     1.12445290E-01    2     1000022   1000023   # BR(H_3 -> neu_1 neu_2)
     1.02952894E-02    2     1000022   1000025   # BR(H_3 -> neu_1 neu_3)
     8.44269669E-03    2     1000022   1000035   # BR(H_3 -> neu_1 neu_4)
     2.15559232E-02    2     1000023   1000023   # BR(H_3 -> neu_2 neu_2)
     4.68154423E-02    2     1000023   1000025   # BR(H_3 -> neu_2 neu_3)
     1.47130705E-02    2     1000023   1000035   # BR(H_3 -> neu_2 neu_4)
     5.90511461E-03    2     1000025   1000025   # BR(H_3 -> neu_3 neu_3)
     2.43478898E-03    2     1000025   1000035   # BR(H_3 -> neu_3 neu_4)
     1.30356635E-04    2     1000024  -1000024   # BR(H_3 -> cha_1 cha_1bar)
DECAY        36     3.18602515E-04   # Lightest pseudoscalar
     2.36709580E-03    2          21        21   # BR(A_1 -> gluon gluon)
     3.27434615E-04    2          13       -13   # BR(A_1 -> muon muon)
     9.25655162E-02    2          15       -15   # BR(A_1 -> tau tau)
     6.94617399E-04    2           3        -3   # BR(A_1 -> s sbar)
     1.03263460E-03    2           4        -4   # BR(A_1 -> c cbar)
     9.02634951E-01    2           5        -5   # BR(A_1 -> b bbar)
     0.00000000E+00    2           6        -6   # BR(A_1 -> t tbar)
     3.77694161E-04    2          22        22   # BR(A_1 -> gamma gamma)
     5.65045906E-08    2          23        22   # BR(A_1 -> Z gamma)
DECAY        46     8.81632847E+00   # 2nd pseudoscalar
     9.54823797E-04    2          21        21   # BR(A_2 -> gluon gluon)
     3.17831997E-06    2          13       -13   # BR(A_2 -> muon muon)
     8.98965544E-04    2          15       -15   # BR(A_2 -> tau tau)
     5.05443789E-06    2           3        -3   # BR(A_2 -> s sbar)
     1.52822541E-04    2           4        -4   # BR(A_2 -> c cbar)
     6.67178126E-03    2           5        -5   # BR(A_2 -> b bbar)
     4.50266878E-01    2           6        -6   # BR(A_2 -> t tbar)
     3.98012780E-06    2          22        22   # BR(A_2 -> gamma gamma)
     1.17649693E-06    2          23        22   # BR(A_2 -> Z gamma)
     2.25087905E-02    2          36        25   # BR(A_2 -> A_1 H_1)
     1.09466000E-01    2          36        35   # BR(A_2 -> A_1 H_2)
     1.13431551E-01    2          23        25   # BR(A_2 -> Z H_1)
     2.67097655E-03    2          23        35   # BR(A_2 -> Z H_2)
     1.18590367E-01    2     1000022   1000022   # BR(A_2 -> neu_1 neu_1)
     6.52708269E-03    2     1000022   1000023   # BR(A_2 -> neu_1 neu_2)
     8.26448438E-02    2     1000022   1000025   # BR(A_2 -> neu_1 neu_3)
     8.21962411E-03    2     1000022   1000035   # BR(A_2 -> neu_1 neu_4)
     7.82959022E-03    2     1000023   1000023   # BR(A_2 -> neu_2 neu_2)
     1.98181406E-02    2     1000023   1000025   # BR(A_2 -> neu_2 neu_3)
     1.90788361E-03    2     1000023   1000035   # BR(A_2 -> neu_2 neu_4)
     3.33805029E-02    2     1000025   1000025   # BR(A_2 -> neu_3 neu_3)
     1.36380872E-02    2     1000025   1000035   # BR(A_2 -> neu_3 neu_4)
     4.07898649E-04    2     1000024  -1000024   # BR(A_2 -> cha_1 cha_1bar)
DECAY        37     8.13489547E+00   # Charged Higgs
     3.44401841E-06    2         -13        14   # BR(H+ -> muon nu_muon)
     9.74115749E-04    2         -15        16   # BR(H+ -> tau nu_tau)
     2.62686498E-07    2           2        -3   # BR(H+ -> u sbar)
     1.05038428E-05    2           4        -3   # BR(H+ -> c sbar)
     1.11252746E-07    2           2        -5   # BR(H+ -> u bbar)
     1.11347658E-05    2           4        -5   # BR(H+ -> c bbar)
     4.65101290E-01    2           6        -5   # BR(H+ -> t bbar)
     1.19657174E-01    2          24        25   # BR(H+ -> W+ H_1)
     2.81269434E-03    2          24        35   # BR(H+ -> W+ H_2)
     1.17185318E-01    2          24        36   # BR(H+ -> W+ A_1)
     2.30363263E-01    2     1000024   1000022   # BR(H+ -> cha_1 neu_1)
     1.86925126E-02    2     1000024   1000023   # BR(H+ -> cha_1 neu_2)
     2.98949223E-02    2     1000024   1000025   # BR(H+ -> cha_1 neu_3)
     1.52932531E-02    2     1000024   1000035   # BR(H+ -> cha_1 neu_4)
DECAY         6     1.38766019E+00   # Top Quark
     1.00000000E+00    2           5        24   # BR(t ->  b    W+)
#         PDG            Width
DECAY        24     2.08500000E+00   # W+ (measured)
     1.16500000E-01    2         -11        12   # BR(W+ -> e+ nu_e)
     1.16500000E-01    2         -13        14   # BR(W+ -> mu+ nu_mu)
     1.12000000E-01    2         -15        16   # BR(W+ -> tau+ nu_tau)
     3.65000000E-01    2           2        -1   # BR(W+ -> u db)
     3.10000000E-01    2           4        -3   # BR(W+ -> c sb)
#         PDG            Width
DECAY        23     2.49520000E+00   # Z (measured)
     2.00000000E-01    2         -12        12   # BR(Z -> invisible)
     3.36500000E-02    2         -11        11   # BR(Z -> e+ e-)
     3.36500000E-02    2         -13        13   # BR(Z -> mu+ mu-)
     3.37000000E-02    2         -15        15   # BR(Z -> tau+ tau-)
     1.11000000E-01    2           2        -2   # BR(Z -> u ub)
     1.58500000E-01    2           1        -1   # BR(Z -> d db)
     1.58500000E-01    2           3        -3   # BR(Z -> s sb)
     1.20000000E-01    2           4        -4   # BR(Z -> c cb)
     1.51000000E-01    2           5        -5   # BR(Z -> b bb)
#         PDG            Width
DECAY   1000024     1.95835259E-01   # chargino1
#                    chargino1 2-body decays
#          BR         NDA      ID1       ID2
     1.00000000E+00    2     1000022        24   # BR(~chi_1+ -> ~chi_10  W+)
#         PDG            Width
DECAY   1000037     2.89345330E+00   # chargino2
#                    chargino2 2-body decays
#          BR         NDA      ID1       ID2
     2.60437272E-01    2     1000024        23   # BR(~chi_2+ -> ~chi_1+  Z )
     1.03236906E-01    2     1000022        24   # BR(~chi_2+ -> ~chi_10  W+)
     1.95562869E-01    2     1000023        24   # BR(~chi_2+ -> ~chi_20  W+)
     1.82844678E-01    2     1000025        24   # BR(~chi_2+ -> ~chi_30  W+)
     3.53089940E-02    2     1000035        24   # BR(~chi_2+ -> ~chi_40  W+)
     6.49625506E-03    2     1000024        25   # BR(~chi_2+ -> ~chi_1+  H_1 )
     2.15703041E-01    2     1000024        35   # BR(~chi_2+ -> ~chi_1+  H_2 )
     4.09984517E-04    2     1000024        36   # BR(~chi_2+ -> ~chi_1+  A_1 )
#         PDG            Width
DECAY   1000022     0.00000000E+00   # neutralino1
#         PDG            Width
DECAY   1000023     2.80709100E-01   # neutralino2
#                    neutralino2 2-body decays
#          BR         NDA      ID1       ID2
     6.04265538E-01    2     1000022        23   # BR(~chi_20 -> ~chi_10   Z )
     2.95639722E-01    2     1000022        25   # BR(~chi_20 -> ~chi_10   H_1 )
     9.64463150E-02    2     1000022        35   # BR(~chi_20 -> ~chi_10   H_2 )
     3.64842501E-03    2     1000022        36   # BR(~chi_20 -> ~chi_10   A_1 )
#         PDG            Width
DECAY   1000025     2.22299883E-01   # neutralino3
#                    neutralino3 2-body decays
#          BR         NDA      ID1       ID2
     2.84367308E-01    2     1000022        23   # BR(~chi_30 -> ~chi_10   Z )
     6.35599398E-02    2     1000022        25   # BR(~chi_30 -> ~chi_10   H_1 )
     1.06855872E-02    2     1000022        35   # BR(~chi_30 -> ~chi_10   H_2 )
     6.41387165E-01    2     1000022        36   # BR(~chi_30 -> ~chi_10   A_1 )
#         PDG            Width
DECAY   1000035     7.91119907E-02   # neutralino4
#                    neutralino4 2-body decays
#          BR         NDA      ID1       ID2
     4.28120229E-01    2     1000022        23   # BR(~chi_40 -> ~chi_10   Z )
     2.25372047E-01    2     1000024       -24   # BR(~chi_40 -> ~chi_1+   W-)
     2.25372047E-01    2    -1000024        24   # BR(~chi_40 -> ~chi_1-   W+)
     3.03693160E-03    2     1000022        25   # BR(~chi_40 -> ~chi_10   H_1 )
     9.15655213E-04    2     1000022        35   # BR(~chi_40 -> ~chi_10   H_2 )
     1.17183090E-01    2     1000022        36   # BR(~chi_40 -> ~chi_10   A_1 )
#         PDG            Width
DECAY   1000045     2.89796994E+00   # neutralino5
#                    neutralino5 2-body decays
#          BR         NDA      ID1       ID2
     6.33013781E-02    2     1000022        23   # BR(~chi_50 -> ~chi_10   Z )
     7.93077851E-02    2     1000023        23   # BR(~chi_50 -> ~chi_20   Z )
     1.12576454E-01    2     1000025        23   # BR(~chi_50 -> ~chi_30   Z )
     6.89245780E-03    2     1000035        23   # BR(~chi_50 -> ~chi_40   Z )
     2.58445302E-01    2     1000024       -24   # BR(~chi_50 -> ~chi_1+   W-)
     2.58445302E-01    2    -1000024        24   # BR(~chi_50 -> ~chi_1-   W+)
     1.73722568E-03    2     1000022        25   # BR(~chi_50 -> ~chi_10   H_1 )
     3.30178542E-02    2     1000022        35   # BR(~chi_50 -> ~chi_10   H_2 )
     7.47404421E-04    2     1000022        36   # BR(~chi_50 -> ~chi_10   A_1 )
     2.53409736E-03    2     1000023        25   # BR(~chi_50 -> ~chi_20   H_1 )
     8.92971873E-02    2     1000023        35   # BR(~chi_50 -> ~chi_20   H_2 )
     3.84470220E-07    2     1000023        36   # BR(~chi_50 -> ~chi_20   A_1 )
     1.39775773E-03    2     1000025        25   # BR(~chi_50 -> ~chi_30   H_1 )
     6.49205622E-02    2     1000025        35   # BR(~chi_50 -> ~chi_30   H_2 )
     1.65607971E-04    2     1000025        36   # BR(~chi_50 -> ~chi_30   A_1 )
     6.91563570E-04    2     1000035        25   # BR(~chi_50 -> ~chi_40   H_1 )
     2.65102260E-02    2     1000035        35   # BR(~chi_50 -> ~chi_40   H_2 )
     1.14493273E-05    2     1000035        36   # BR(~chi_50 -> ~chi_40   A_1 )
#         PDG            Width
DECAY   1000021     1.50428324E+00   # gluino
#                    gluino 2-body decays
#          BR         NDA      ID1       ID2
     4.15019481E-02    2     1000001        -1   # BR(~g -> ~d_L  db)
     4.15019481E-02    2    -1000001         1   # BR(~g -> ~d_L* d )
     4.34493601E-02    2     2000001        -1   # BR(~g -> ~d_R  db)
     4.34493601E-02    2    -2000001         1   # BR(~g -> ~d_R* d )
     4.58956155E-02    2     1000002        -2   # BR(~g -> ~u_L  ub)
     4.58956155E-02    2    -1000002         2   # BR(~g -> ~u_L* u )
     4.47851326E-02    2     2000002        -2   # BR(~g -> ~u_R  ub)
     4.47851326E-02    2    -2000002         2   # BR(~g -> ~u_R* u )
     4.15019481E-02    2     1000003        -3   # BR(~g -> ~s_L  sb)
     4.15019481E-02    2    -1000003         3   # BR(~g -> ~s_L* s )
     4.34493601E-02    2     2000003        -3   # BR(~g -> ~s_R  sb)
     4.34493601E-02    2    -2000003         3   # BR(~g -> ~s_R* s )
     4.58956155E-02    2     1000004        -4   # BR(~g -> ~c_L  cb)
     4.58956155E-02    2    -1000004         4   # BR(~g -> ~c_L* c )
     4.47851326E-02    2     2000004        -4   # BR(~g -> ~c_R  cb)
     4.47851326E-02    2    -2000004         4   # BR(~g -> ~c_R* c )
     5.06109135E-02    2     1000005        -5   # BR(~g -> ~b_1  bb)
     5.06109135E-02    2    -1000005         5   # BR(~g -> ~b_1* b )
     3.44326111E-02    2     2000005        -5   # BR(~g -> ~b_2  bb)
     3.44326111E-02    2    -2000005         5   # BR(~g -> ~b_2* b )
#                    gluino 3-body decays
#           BR         NDA      ID1       ID2       ID3
     1.77835625E-02    3     1000022         6        -6   # BR(~g -> ~chi_10 t  tb)
     2.92208677E-02    3     1000023         6        -6   # BR(~g -> ~chi_20 t  tb)
     3.19808542E-02    3     1000025         6        -6   # BR(~g -> ~chi_30 t  tb)
     1.01640829E-02    3     1000035         6        -6   # BR(~g -> ~chi_40 t  tb)
     1.82929178E-03    3     1000045         6        -6   # BR(~g -> ~chi_50 t  tb)
     1.57423649E-02    3     1000024         5        -6   # BR(~g -> ~chi_1+ b  tb)
     1.57423649E-02    3    -1000024         6        -5   # BR(~g -> ~chi_1- t  bb)
     2.43024674E-03    3     1000037         5        -6   # BR(~g -> ~chi_2+ b  tb)
     2.43024674E-03    3    -1000037         6        -5   # BR(~g -> ~chi_2- t  bb)
     3.04215367E-05    3     1000006        -5       -24   # BR(~g -> ~t_1    bb W-)
     3.04215367E-05    3    -1000006         5        24   # BR(~g -> ~t_1*   b  W+)
#         PDG            Width
DECAY   1000011     5.78662127E+00   # selectron_L
#                    selectron_L 2-body decays
#          BR         NDA      ID1       ID2
     3.06853420E-04    2     1000022        11   # BR(~e_L -> ~chi_10 e-)   
     1.09569599E-03    2     1000023        11   # BR(~e_L -> ~chi_20 e-)   
     1.30820018E-03    2     1000025        11   # BR(~e_L -> ~chi_30 e-)  
     2.02128255E-01    2     1000035        11   # BR(~e_L -> ~chi_40 e-)  
     2.59433459E-01    2     1000045        11   # BR(~e_L -> ~chi_50 e-)  
     1.25739990E-04    2    -1000024        12   # BR(~e_L -> ~chi_1- nu_e)
     5.35601797E-01    2    -1000037        12   # BR(~e_L -> ~chi_2- nu_e)
#         PDG            Width
DECAY   2000011     4.32983960E+00   # selectron_R
#                    selectron_R 2-body decays
#          BR         NDA      ID1       ID2
     2.29457483E-03    2     1000022        11   # BR(~e_R -> ~chi_10 e-)
     5.09644901E-03    2     1000023        11   # BR(~e_R -> ~chi_20 e-)
     4.35807371E-02    2     1000025        11   # BR(~e_R -> ~chi_30 e-)
     9.48925406E-01    2     1000035        11   # BR(~e_R -> ~chi_40 e-)
     1.02833009E-04    2     1000045        11   # BR(~e_R -> ~chi_50 e-)
#         PDG            Width
DECAY   1000013     5.78662127E+00   # smuon_L
#                    smuon_L 2-body decays
#          BR         NDA      ID1       ID2
     3.06853420E-04    2     1000022        13   # BR(~mu_L -> ~chi_10 mu-)
     1.09569599E-03    2     1000023        13   # BR(~mu_L -> ~chi_20 mu-)
     1.30820018E-03    2     1000025        13   # BR(~mu_L -> ~chi_30 mu-)
     2.02128255E-01    2     1000035        13   # BR(~mu_L -> ~chi_40 mu-)
     2.59433459E-01    2     1000045        13   # BR(~mu_L -> ~chi_50 mu-)
     1.25739990E-04    2    -1000024        14   # BR(~mu_L -> ~chi_1- nu_mu)
     5.35601797E-01    2    -1000037        14   # BR(~mu_L -> ~chi_2- nu_mu)
#         PDG            Width
DECAY   2000013     4.32983960E+00   # smuon_R
#                    smuon_R 2-body decays
#          BR         NDA      ID1       ID2
     2.29457483E-03    2     1000022        13   # BR(~mu_R -> ~chi_10 mu-)
     5.09644901E-03    2     1000023        13   # BR(~mu_R -> ~chi_20 mu-)
     4.35807371E-02    2     1000025        13   # BR(~mu_R -> ~chi_30 mu-)
     9.48925406E-01    2     1000035        13   # BR(~mu_R -> ~chi_40 mu-)
     1.02833009E-04    2     1000045        13   # BR(~mu_R -> ~chi_50 mu-)
#         PDG            Width
DECAY   1000015     5.03147228E+00   # stau_1
#                    stau1 2-body decays
#          BR         NDA      ID1       ID2
     1.14223615E-03    2     1000022        15   # BR(~tau_1 -> ~chi_10  tau-)
     4.79773891E-04    2     1000023        15   # BR(~tau_1 -> ~chi_20  tau-)
     2.71137489E-02    2     1000025        15   # BR(~tau_1 -> ~chi_30  tau-)
     5.31309722E-01    2     1000035        15   # BR(~tau_1 -> ~chi_40  tau-)
     1.43316980E-01    2     1000045        15   # BR(~tau_1 -> ~chi_50  tau-)
     8.82647177E-04    2    -1000024        16   # BR(~tau_1 -> ~chi_1-  nu_tau)
     2.95754892E-01    2    -1000037        16   # BR(~tau_1 -> ~chi_2-  nu_tau)
#         PDG            Width
DECAY   2000015     4.34587474E+00   # stau_2
#                    stau_2 2-body decays
#          BR         NDA      ID1       ID2
     1.37392831E-03    2     1000022        15   # BR(~tau_2 -> ~chi_10  tau-)
     9.20702858E-03    2     1000023        15   # BR(~tau_2 -> ~chi_20  tau-)
     1.68745751E-02    2     1000025        15   # BR(~tau_2 -> ~chi_30  tau-)
     5.99525384E-01    2     1000035        15   # BR(~tau_2 -> ~chi_40  tau-)
     1.79551664E-01    2     1000045        15   # BR(~tau_2 -> ~chi_50  tau-)
     2.39224331E-03    2    -1000024        16   # BR(~tau_2 -> ~chi_1-  nu_tau)
     3.70626840E-01    2    -1000037        16   # BR(~tau_2 -> ~chi_2-  nu_tau)
#         PDG            Width
DECAY   1000012     5.82409806E+00   # snu_eL
#                    snu_eL 2-body decays
#          BR         NDA      ID1       ID2
     3.44541021E-03    2     1000022        12   # BR(~nu_eL -> ~chi_10 nu_e)
     8.91602588E-03    2     1000023        12   # BR(~nu_eL -> ~chi_20 nu_e)
     2.06692014E-02    2     1000025        12   # BR(~nu_eL -> ~chi_30 nu_e)
     1.53093689E-01    2     1000035        12   # BR(~nu_eL -> ~chi_40 nu_e)
     2.64584107E-01    2     1000045        12   # BR(~nu_eL -> ~chi_50 nu_e)
     3.61604589E-02    2     1000024        11   # BR(~nu_eL -> ~chi_1+ e-)
     5.13131108E-01    2     1000037        11   # BR(~nu_eL -> ~chi_2+ e-)
#         PDG            Width
DECAY   1000014     5.82409806E+00   # snu_muL
#                    snu_muL 2-body decays
#          BR         NDA      ID1       ID2
     3.44541021E-03    2     1000022        14   # BR(~nu_muL -> ~chi_10 nu_mu)
     8.91602588E-03    2     1000023        14   # BR(~nu_muL -> ~chi_20 nu_mu)
     2.06692014E-02    2     1000025        14   # BR(~nu_muL -> ~chi_30 nu_mu)
     1.53093689E-01    2     1000035        14   # BR(~nu_muL -> ~chi_40 nu_mu)
     2.64584107E-01    2     1000045        14   # BR(~nu_muL -> ~chi_50 nu_mu)
     3.61604589E-02    2     1000024        13   # BR(~nu_muL -> ~chi_1+ mu-)
     5.13131108E-01    2     1000037        13   # BR(~nu_muL -> ~chi_2+ mu-)
#         PDG            Width
DECAY   1000016     5.83820352E+00   # snu_tauL
#                    sbu_tauL 2-body decays
#          BR         NDA      ID1       ID2
     3.43708589E-03    2     1000022        16   # BR(~nu_tauL -> ~chi_10 nu_tau)
     8.89448421E-03    2     1000023        16   # BR(~nu_tauL -> ~chi_20 nu_tau)
     2.06192633E-02    2     1000025        16   # BR(~nu_tauL -> ~chi_30 nu_tau)
     1.52723805E-01    2     1000035        16   # BR(~nu_tauL -> ~chi_40 nu_tau)
     2.63944855E-01    2     1000045        16   # BR(~nu_tauL -> ~chi_50 nu_tau)
     3.84961084E-02    2     1000024        15   # BR(~nu_tauL -> ~chi_1+ tau-)
     5.11884398E-01    2     1000037        15   # BR(~nu_tauL -> ~chi_2+ tau-)
#         PDG            Width
DECAY   1000002     5.73690169E+00   # sup_L
#                    sup_L 2-body decays
#          BR         NDA      ID1       ID2
     9.95251790E-04    2     1000022         2   # BR(~u_L -> ~chi_10 u)
     2.97343586E-03    2     1000023         2   # BR(~u_L -> ~chi_20 u)
     5.95852786E-04    2     1000025         2   # BR(~u_L -> ~chi_30 u)
     2.97748113E-02    2     1000035         2   # BR(~u_L -> ~chi_40 u)
     3.11048066E-01    2     1000045         2   # BR(~u_L -> ~chi_50 u)
     3.75280135E-02    2     1000024         1   # BR(~u_L -> ~chi_1+ d)
     6.17084569E-01    2     1000037         1   # BR(~u_L -> ~chi_2+ d)
#         PDG            Width
DECAY   2000002     1.99702792E+00   # sup_R
#                    sup_R 2-body decays
#          BR         NDA      ID1       ID2
     2.22404073E-03    2     1000022         2   # BR(~u_R -> ~chi_10 u)
     5.02648426E-03    2     1000023         2   # BR(~u_R -> ~chi_20 u)
     4.29887117E-02    2     1000025         2   # BR(~u_R -> ~chi_30 u)
     9.49644059E-01    2     1000035         2   # BR(~u_R -> ~chi_40 u)
     1.16703911E-04    2     1000045         2   # BR(~u_R -> ~chi_50 u)
#         PDG            Width
DECAY   1000001     5.64341676E+00   # sdown_L
#                    sdown_L 2-body decays
#          BR         NDA      ID1       ID2
     2.10434166E-03    2     1000022         1   # BR(~d_L -> ~chi_10 d)
     5.79758640E-03    2     1000023         1   # BR(~d_L -> ~chi_20 d)
     7.45741604E-03    2     1000025         1   # BR(~d_L -> ~chi_30 d)
     1.34387644E-02    2     1000035         1   # BR(~d_L -> ~chi_40 d)
     3.21776483E-01    2     1000045         1   # BR(~d_L -> ~chi_50 d)
     1.31720072E-04    2    -1000024         2   # BR(~d_L -> ~chi_1- u)
     6.49293689E-01    2    -1000037         2   # BR(~d_L -> ~chi_2- u)
#         PDG            Width
DECAY   2000001     4.99627981E-01   # sdown_R
#                    sdown_R 2-body decays
#          BR         NDA      ID1       ID2
     2.22360755E-03    2     1000022         1   # BR(~d_R -> ~chi_10 d)
     5.02599176E-03    2     1000023         1   # BR(~d_R -> ~chi_20 d)
     4.29845407E-02    2     1000025         1   # BR(~d_R -> ~chi_30 d)
     9.49649027E-01    2     1000035         1   # BR(~d_R -> ~chi_40 d)
     1.16832589E-04    2     1000045         1   # BR(~d_R -> ~chi_50 d)
#         PDG            Width
DECAY   1000004     5.73690169E+00   # scharm_L
#                    scharm_L 2-body decays
#          BR         NDA      ID1       ID2
     9.95251790E-04    2     1000022         4   # BR(~c_L -> ~chi_10 c)
     2.97343586E-03    2     1000023         4   # BR(~c_L -> ~chi_20 c)
     5.95852786E-04    2     1000025         4   # BR(~c_L -> ~chi_30 c)
     2.97748113E-02    2     1000035         4   # BR(~c_L -> ~chi_40 c)
     3.11048066E-01    2     1000045         4   # BR(~c_L -> ~chi_50 c)
     3.75280135E-02    2     1000024         3   # BR(~c_L -> ~chi_1+ s)
     6.17084569E-01    2     1000037         3   # BR(~c_L -> ~chi_2+ s)
#         PDG            Width
DECAY   2000004     1.99702792E+00   # scharm_R
#                    scharm_R 2-body decays
#          BR         NDA      ID1       ID2
     2.22404073E-03    2     1000022         4   # BR(~c_R -> ~chi_10 c)
     5.02648426E-03    2     1000023         4   # BR(~c_R -> ~chi_20 c)
     4.29887117E-02    2     1000025         4   # BR(~c_R -> ~chi_30 c)
     9.49644059E-01    2     1000035         4   # BR(~c_R -> ~chi_40 c)
     1.16703911E-04    2     1000045         4   # BR(~c_R -> ~chi_50 c)
#         PDG            Width
DECAY   1000003     5.64341676E+00   # sstrange_L
#                    sstrange_L 2-body decays
#          BR         NDA      ID1       ID2
     2.10434166E-03    2     1000022         3   # BR(~s_L -> ~chi_10 s)
     5.79758640E-03    2     1000023         3   # BR(~s_L -> ~chi_20 s)
     7.45741604E-03    2     1000025         3   # BR(~s_L -> ~chi_30 s)
     1.34387644E-02    2     1000035         3   # BR(~s_L -> ~chi_40 s)
     3.21776483E-01    2     1000045         3   # BR(~s_L -> ~chi_50 s)
     1.31720072E-04    2    -1000024         4   # BR(~s_L -> ~chi_1- c)
     6.49293689E-01    2    -1000037         4   # BR(~s_L -> ~chi_2- c)
#         PDG            Width
DECAY   2000003     4.99627981E-01   # sstrange_R
#                    sstrange_R 2-body decays
#          BR         NDA      ID1       ID2
     2.22360755E-03    2     1000022         3   # BR(~s_R -> ~chi_10 s)
     5.02599176E-03    2     1000023         3   # BR(~s_R -> ~chi_20 s)
     4.29845407E-02    2     1000025         3   # BR(~s_R -> ~chi_30 s)
     9.49649027E-01    2     1000035         3   # BR(~s_R -> ~chi_40 s)
     1.16832589E-04    2     1000045         3   # BR(~s_R -> ~chi_50 s)
#         PDG            Width
DECAY   1000006     2.19507250E+01   # stop1
#                    stop1 2-body decays
#          BR         NDA      ID1       ID2
     1.09835047E-01    2     1000022         6   # BR(~t_1 -> ~chi_10 t )
     1.96137940E-01    2     1000023         6   # BR(~t_1 -> ~chi_20 t )
     2.17475234E-01    2     1000025         6   # BR(~t_1 -> ~chi_30 t )
     8.77600394E-02    2     1000035         6   # BR(~t_1 -> ~chi_40 t )
     4.58507526E-02    2     1000045         6   # BR(~t_1 -> ~chi_50 t )
     2.51855409E-01    2     1000024         5   # BR(~t_1 -> ~chi_1+ b )
     9.10855776E-02    2     1000037         5   # BR(~t_1 -> ~chi_2+ b )
#         PDG            Width
DECAY   2000006     3.20646259E+01   # stop2
#                    stop2 2-body decays
#          BR         NDA      ID1       ID2
     1.11194336E-01    2     1000022         6   # BR(~t_2 -> ~chi_10 t )
     2.29610086E-01    2     1000023         6   # BR(~t_2 -> ~chi_20 t )
     2.08124698E-01    2     1000025         6   # BR(~t_2 -> ~chi_30 t )
     2.99776056E-02    2     1000035         6   # BR(~t_2 -> ~chi_40 t )
     2.13391355E-02    2     1000045         6   # BR(~t_2 -> ~chi_50 t )
     3.27175445E-01    2     1000024         5   # BR(~t_2 -> ~chi_1+ b )
     3.69842728E-02    2     1000037         5   # BR(~t_2 -> ~chi_2+ b )
     7.39664766E-08    2     1000006        25   # BR(~t_2 -> ~t_1    H1 )
     3.66877808E-07    2     1000006        35   # BR(~t_2 -> ~t_1    H2 )
     1.12679731E-12    2     1000006        36   # BR(~t_2 -> ~t_1    A1 )
     3.33268254E-02    2     1000006        23   # BR(~t_2 -> ~t_1    Z )
     1.29689102E-03    2     1000005        24   # BR(~t_2 -> ~b_1    W+)
     9.70265011E-04    2     2000005        24   # BR(~t_2 -> ~b_2    W+)
#         PDG            Width
DECAY   1000005     7.88244843E+00   # sbottom1
#                    sbottom1 2-body decays
#          BR         NDA      ID1       ID2
     5.94766677E-04    2     1000022         5   # BR(~b_1 -> ~chi_10 b )
     1.58466058E-04    2     1000023         5   # BR(~b_1 -> ~chi_20 b )
     1.03987068E-02    2     1000025         5   # BR(~b_1 -> ~chi_30 b )
     3.90629873E-02    2     1000035         5   # BR(~b_1 -> ~chi_40 b )
     7.88040133E-02    2     1000045         5   # BR(~b_1 -> ~chi_50 b )
     7.01586865E-01    2    -1000024         6   # BR(~b_1 -> ~chi_1- t )
     1.69394195E-01    2    -1000037         6   # BR(~b_1 -> ~chi_2- t )
#         PDG            Width
DECAY   2000005     1.27481096E+01   # sbottom2
#                    sbottom2 2-body decays
#          BR         NDA      ID1       ID2
     6.43899381E-04    2     1000022         5   # BR(~b_2 -> ~chi_10 b )
     4.83381564E-03    2     1000023         5   # BR(~b_2 -> ~chi_20 b )
     6.51444983E-04    2     1000025         5   # BR(~b_2 -> ~chi_30 b )
     1.82128831E-02    2     1000035         5   # BR(~b_2 -> ~chi_40 b )
     8.44763547E-02    2     1000045         5   # BR(~b_2 -> ~chi_50 b )
     7.08886289E-01    2    -1000024         6   # BR(~b_2 -> ~chi_1- t )
     1.81714614E-01    2    -1000037         6   # BR(~b_2 -> ~chi_2- t )
#
# Dummy alpha block (for Prospino compatibility only - not used)
BLOCK ALPHA
	0.1000E+00
"""

  f = open("%s/src/WorkingPoint_mH1_95_mH2_125p3_MSUSY_1000.slha" % os.environ['CMSSW_BASE'],"w")
  f.write(slhacontent)
  f.close()
  
  return process