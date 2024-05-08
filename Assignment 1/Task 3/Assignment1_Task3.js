NRF.findDevices(function(devices) {
  print(devices);
}, { filters: [{ services: ['6e400001-b5a3-f393-e0a9-e50e24dcca9e'] }], timeout: 2000, active:true });

i = 0;

setInterval(function() {
    if (i == 0){
      sample = "";
    }
    var accel = Puck.accel().acc;
    if (i < 20)
    {
      var x = ((accel.x-(-32768))/(32767-(-32768)))*(127-(-127))+(-127);
      var y = ((accel.y-(-32768))/(32767-(-32768)))*(127-(-127))+(-127);
      var z = ((accel.z-(-32768))/(32767-(-32768)))*(127-(-127))+(-127);
      if (i == 19) {
        sample += x + "," + y + "," + z;
      } else {
        sample += x + "," + y + "," + z + ",";
      }
      i++;
    }
    else {
      print("Ready");
    }
  }, 500);

function getData() {
  i = 0;
  return sample;
}