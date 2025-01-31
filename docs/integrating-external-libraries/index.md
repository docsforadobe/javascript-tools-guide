<a id="integrating-external-libraries"></a>

# Integrating External Libraries

You can extend the JavaScript DOM for an application by writing a C or C++ shared library, compiling it for
the platform you are using, and loading it into JavaScript as an ExternalObject object. A shared library is
implemented by a DLL in Windows, a bundle or framework in Mac OS, or a SharedObject in UNIX.

You can access the library functions directly through the ExternalObject instance, or you can define an
interface that allows your C/C++ code to create and access JavaScript classes and objects.

All Adobe Creative Suite 4 applications support this feature.

## Example code

The sample code distributed with the [Adobe ExtendScript SDK](https://github.com/Adobe-CEP/CEP-Resources/tree/master/ExtendScript-Toolkit) includes an example that demonstrates
how write a C/C++ shared library to be integrated with JavaScript. It is in the directory:

```default
sdkInstall/sdksamples/cpp/
```

The sample shows how to write a plug-in for Adobe Bridge in C/C++, using the ExternalObject
mechanism, which enables the C/C++ code to be called from the JavaScript context. Project files for
Microsoft Visual Studio 2005 and XCode 2.4 are included in subfolders of `sdkInstall/sdksamples/cpp/build.`
