import ROOT
from ROOT import TCanvas, TH1F
from ROOT import gROOT, gRandom

h = ROOT.TH1F("h", "h", 100, -5, 5)
for i in range(1000000):
    d = gRandom.Gaus(0)
    h.Fill(d)