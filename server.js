var express = require('express');
var app = express();


app.listen(3000, function () {
  console.log('server running on port 3000');
})

app.get('/5year',call5year);
app.get('/1year',call1year)

function call5year(req,res){
    //console.log(req,res,next,err)
  var spawn = require('child_process').spawn;
  var process = spawn('python',["./dataProcessing.py",5])
  var called = false
  process.stdout.on('data', function (data) {
    if(!called){
      called=true
      console.log('got here')
      res.send(data.toString());
      console.log("got HERE")
    }
  });
  // process.stdout.on('data', function (data) {
  //   console.log('stdout: ' + data.toString());
  // });

  process.stderr.on('data', function (data) {
    console.log('stderr: '+data);
  });

  process.on('exit', function (code) {
    console.log('child process exited with code ' + code.toString());
  });

}

function call1year(req,res){
    //console.log(req,res,next,err)
  var spawn = require('child_process').spawn;
  var process = spawn('python',["./dataProcessing.py",1])
  var called = false
  process.stdout.on('data', function (data) {
    if(!called){
      called=true
      console.log('got here')
      res.send(data.toString());
      console.log("got HERE")
    }
  });
  // process.stdout.on('data', function (data) {
  //   console.log('stdout: ' + data.toString());
  // });

  process.stderr.on('data', function (data) {
    console.log('stderr: '+data);
  });

  process.on('exit', function (code) {
    console.log('child process exited with code ' + code.toString());
  });


  // }
}
