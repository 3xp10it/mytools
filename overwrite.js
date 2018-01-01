if (ObjC.available)
{
    try
    {
        var className = "PARSPedometerInfo";
        var funcName = "- integratedSteps";
        var hook = eval('ObjC.classes.' + className + '["' + funcName + '"]');
        Interceptor.attach(hook.implementation, {
          onEnter: function(args) {
            console.log("Original args0-> type:"+typeof args[0]+" value:"+args[0])

            newargs0=ptr('xxx')
            args[0]=newargs0
            console.log("New args0-> type:"+typeof args[0]+" value:"+args[0]")
          },
          onLeave: function(retval) {
            console.log("Original retval-> type:"+typeof args[0]+" value:"+args[0])

            newretval=ptr("xxxx")
            retval.replace(newretval)
            console.log("New retval-> type:"+typeof args[0]+" value:"+newretval)
          }
        });
    }
    catch(err)
    {
        console.log("[!] Exception2: " + err.message);
    }
}
else
{
    console.log("Objective-C Runtime is not available!");
}

