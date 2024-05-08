i = 0;

var interval = setInterval(function() {
  var accel = Puck.accel().acc;
  if (i < 20)
  {
    var x = Math.floor(((accel.x-(-32768))/(32767-(-32768)))*(127-(-127))+(-127));
    var y = Math.floor(((accel.y-(-32768))/(32767-(-32768)))*(127-(-127))+(-127));
    var z = Math.floor(((accel.z-(-32768))/(32767-(-32768)))*(127-(-127))+(-127));
    var sample = { x: x, y: y, z: z };
    print("Sample number " + i + ": ", sample);
    Infxl.insert(i, x, y, z);
    i++;
  }
  else
  {
    print("Classification result: " + Infxl.model());
    i = 0;
  }
}, 500);