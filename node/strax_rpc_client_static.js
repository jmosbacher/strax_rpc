
var messages = require('./strax_rpc_pb');
var services = require('./strax_rpc_grpc_pb');

var async = require('async');
var _ = require('lodash');
var grpc = require('grpc');

var client = new services.StraxRPCClient('localhost:50051',
                                           grpc.credentials.createInsecure());


/** 
* @param {function} callback Called when this demo is complete
*/

function runSearchField(callback) {
    const pattern = "s1*";
    var spat = new messages.SearchPattern();
    spat.setPattern(pattern);
    console.log('Looking for fields that match the pattern '+ pattern);
    var call = client.searchField(spat);
    call.on('data', function(r) {
      console.log(r.getName() + " is part of " + r.getDataName() + " (provided by " + r.getPlugin() + ")");
        });
    call.on('end', callback);
}

function runGetDF(callback) {
    const run_id = "";
    const dframe = ""
    
    call.on('data', function(r) {
      
        });
    call.on('end', callback);
}

function main() {
    async.series([
        runSearchField,
    ]);
  }
  
  if (require.main === module) {
    main();
  }
  
  exports.runSearchField = runSearchField;
  
 