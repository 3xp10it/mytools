const strings = [];
ObjC.choose(ObjC.classes.NSString, {
  onMatch: function (str) {
    strings.push(str);
  },
  onComplete: function () {
    console.log('Found ' + strings.length + ' strings!');
  }
});
