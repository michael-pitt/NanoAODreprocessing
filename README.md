# CMSSW set-up

```
cmsrel CMSSW_10_6_27
cd CMSSW_10_6_27/src
cmsenv
git cms-init
git cms-addpkg PhysicsTools/NanoAOD
scram b -j 8
```


# Get private code

```
git clone https://github.com/cecilecaillol/NanoAODreprocessing.git
cp NanoAODreprocessing/chargedPF_cff.py PhysicsTools/NanoAOD/python/.
cp NanoAODreprocessing/losttracks_cff.py.py PhysicsTools/NanoAOD/python/.
cp NanoAODreprocessing/nano_cff.py.py PhysicsTools/NanoAOD/python/.
cp NanoAODreprocessing/DiTauFilter.cc PhysicsTools/NanoAOD/plugins/.
cp NanoAODreprocessing/IsMatchedToHSProducer.cc PhysicsTools/NanoAOD/plugins/.
cp NanoAODreprocessing/run_crab.py .
rm -rf NanoAODreprocessing
scram b -j 8
```

# Run nanoAOD production

For MC:
```
cmsRun run_crab.py
```
