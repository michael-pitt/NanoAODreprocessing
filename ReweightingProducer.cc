#include "FWCore/Framework/interface/EDProducer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/Run.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "DataFormats/NanoAOD/interface/FlatTable.h"
#include "DataFormats/NanoAOD/interface/MergeableCounterTable.h"
#include "FWCore/ParameterSet/interface/ConfigurationDescriptions.h"
#include "FWCore/ParameterSet/interface/ParameterSetDescription.h"
#include "FWCore/Utilities/interface/transform.h"
#include "SimDataFormats/GeneratorProducts/interface/GenEventInfoProduct.h"
#include "SimDataFormats/GeneratorProducts/interface/LHEEventProduct.h"
#include "SimDataFormats/GeneratorProducts/interface/LHERunInfoProduct.h"
#include "SimDataFormats/GeneratorProducts/interface/GenLumiInfoHeader.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"
#include "boost/algorithm/string.hpp"

#include <vector>
#include <unordered_map>
#include <iostream>
#include <regex>


class ReweightingProducer:
    public edm::EDProducer
{
    protected:
        const std::vector<edm::InputTag> lheLabel_;
        const std::vector<edm::EDGetTokenT<LHEEventProduct>> lheTag_;

    public:
        ReweightingProducer( edm::ParameterSet const & params ) :
            lheLabel_(params.getParameter<std::vector<edm::InputTag>>("lheInfo")),
            lheTag_(edm::vector_transform(lheLabel_,
                                      [this](const edm::InputTag& tag) { return mayConsume<LHEEventProduct>(tag); }))
        {
            produces<nanoaod::FlatTable>();
        }

        ~ReweightingProducer() override {}

        void produce(edm::Event& iEvent, const edm::EventSetup& iSetup) override 
        {
            auto lheWeightTable = std::make_unique<nanoaod::FlatTable>(1,"TauG2Weights",true,false);

            edm::Handle<LHEEventProduct> lheInfo;
            for (const auto& lheTag : lheTag_) {
              iEvent.getByToken(lheTag, lheInfo);
              if (lheInfo.isValid()) {
                break;
              }
            }
            if (lheInfo.isValid()) {

            
               double normWeight = lheInfo->originalXWGTUP();
               std::vector<gen::WeightsInfo> weights = lheInfo->weights();
               for (const auto& weight: weights)
               {
		  std::size_t found = weight.id.find("ceBR");
                  if (found!=std::string::npos) lheWeightTable->addColumnValue<float>(weight.id,weight.wgt/normWeight,weight.id,nanoaod::FlatTable::FloatColumn);
               }
            }          
            
            iEvent.put(std::move(lheWeightTable));
        }

        
        static void fillDescriptions(edm::ConfigurationDescriptions & descriptions) 
        {
            edm::ParameterSetDescription desc;
        }

};

#include "FWCore/Framework/interface/MakerMacros.h"
DEFINE_FWK_MODULE(ReweightingProducer);
