
var PROTO_PATH = __dirname + '/../protos/strax_rpc.proto';

var async = require('async');
var grpc = require('grpc');
var protoLoader = require('@grpc/proto-loader');
var DataFrame = require('dataframe-js').DataFrame;
// Suggested options for similarity to existing grpc.load behavior
var packageDefinition = protoLoader.loadSync(
    PROTO_PATH,
    {keepCase: true,
     longs: String,
     enums: String,
     defaults: true,
     oneofs: true
    });
var protoDescriptor = grpc.loadPackageDefinition(packageDefinition);
// The protoDescriptor object has the full package hierarchy
var straxrpc = protoDescriptor.straxrpc;

var strax = new straxrpc.StraxRPC('localhost:50051',
                                       grpc.credentials.createInsecure());


/** 
* @param {function} callback Called when this demo is complete
*/

function runSearchField(pattern,callback) {
    // const pattern = "s1*";
    var spat = {
        pattern: pattern
    }
    console.log('\nLooking for fields that match the pattern '+ pattern+"...\n");
    var call = strax.searchField(spat);
    call.on('data', function(r) {
      console.log(r.name + " is part of " + r.data_name + " (provided by " + r.plugin + ")");
        });
    call.on('end', callback);
}

function runGetDF(run_id,dframe,callback) {
    // const run_id = "180423_1021";
    // const dframe = "event_basics";
    var call = strax.getDf({run_id:run_id, dframe:dframe})
    var data = {};
    var columns = [];
    call.on('data', function(r) {
        data[r.info.name] = r[r.info.dtype].values;
        columns.push(r.info.name);
      
        });
    
    call.on('end', function(){
        // console.log(columns);
        console.log("\n Got dataframe "+dframe+" back for run id "+run_id+"\n");
        var df = new DataFrame(data, columns);
        df.show();
        callback(df);
    }
     );
}


function main() {
    async.series([
        async.apply(runSearchField,"s1*"),
        async.apply(runGetDF,"180423_1021","event_basics"),
    ]);
  }
  
  if (require.main === module) {
    main();
  }
  
  exports.runSearchField = runSearchField;
  exports.runGetDF = runGetDF;
  
 