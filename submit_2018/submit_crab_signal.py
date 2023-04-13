from CRABClient.UserUtilities import config, getUsernameFromCRIC

config = config()

config.General.requestName = "GGToTauTau_Inclusive_M_50GeV_PTFilter"
config.General.workArea = "crab_projects"
config.General.transferLogs = True
config.General.transferOutputs = True

config.JobType.pluginName = "Analysis"
config.JobType.psetName = "run_crab_mc.py"
config.JobType.maxMemoryMB = 4000
#config.JobType.numCores = 8

config.Data.inputDataset = "/RunIISummer20UL18_TuneCP5_madgraphLO_reweight/cmst3-crab_GGToTauTau_Inclusive_M_50GeV_PTFilter-c15273f0b6812ff053a850f456209388/USER" 
config.Data.outLFNDirBase = "/store/group/cmst3/group/taug2/reNanoAOD/"
#config.Data.outLFNDirBase = "/store/group/cmst3/user/ccaillol/reNanoAOD/"
config.Data.outputDatasetTag = "GGToTauTau_Inclusive_M_50GeV_PTFilter"
config.Data.inputDBS = "phys03"
config.Data.splitting = "FileBased"
config.Data.unitsPerJob = 25
config.Data.publication = False
config.Data.ignoreLocality = True

config.Site.storageSite = "T2_CH_CERN"
config.Site.whitelist = ["T2_*","T3_*"]
