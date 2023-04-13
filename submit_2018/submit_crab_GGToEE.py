from CRABClient.UserUtilities import config, getUsernameFromCRIC

config = config()

config.General.requestName = "GGToEE_Pt-35_Elastic"
config.General.workArea = "crab_projects"
config.General.transferLogs = True
config.General.transferOutputs = True

config.JobType.pluginName = "Analysis"
config.JobType.psetName = "run_crab_mc.py"
config.JobType.maxMemoryMB = 4000
#config.JobType.numCores = 8

config.Data.inputDataset = "/GGToEE_Pt-35_Elastic_13TeV-lpair/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM" 
config.Data.outLFNDirBase = "/store/group/cmst3/group/taug2/reNanoAOD/"
config.Data.outputDatasetTag = "RunIISummer20UL18_NanoAODv9"
config.Data.inputDBS = "global"
config.Data.splitting = "FileBased"
config.Data.unitsPerJob = 3
config.Data.publication = False
config.Data.ignoreLocality = True

config.Site.storageSite = "T2_CH_CERN"
config.Site.whitelist = ["T2_*","T3_*"]
