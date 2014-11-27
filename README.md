DON'T USE THIS FORK!
====================

This fork was originated from the subversion repository, ported to Python3 and had a load of new features added.

Since that work started the main pythonnet repository has been moved from subversion to github independently of this fork.

A new repository has been created (https://github.com/renshawbay/pythonnet) which contains all of the new features and Python 3 work from this fork, but rebased on the pythonnet/pythonnet repository.

It is recommended that you switch to the python3 branch of that repository as that will be the one that's maintained and developed.

pythonnet
=========

**NOTE** The *official* repo is now https://github.com/pythonnet/pythonnet. Changes from this fork of the original sourceforge project will be integrated back into that main repo in due course.

**Features not yet integrated into the main repo**:
- Python 3 support
- Subclassing managed types in Python

--------------------------------------------------------------------------------------------------------

This fork of http://sourceforge.net/projects/pythonnet/ allows easy calling of python functions from C#.

+ All calls to python should be inside a "using (Py.GIL()) {/* Your code here */}" block.
+ Import python modules using dynamic mod = Py.Import("mod"), then you can call functions as normal, eg mod.func(args).
+ Use mod.func(args, Py.kw("keywordargname", keywordargvalue)) to apply keyword arguments.
+ All python objects should be declared as 'dynamic' type.
+ Mathematical operations involving python and literal/managed types must have the python object first, eg np.pi*2 works, 2*np.pi doesn't

EG:
```csharp
static void Main(string[] args)
{
  using (Py.GIL()) {
    dynamic np = Py.Import("numpy");
    dynamic sin = np.sin;
    Console.WriteLine(np.cos(np.pi*2));
    Console.WriteLine(sin(5));
    double c = np.cos(5) + sin(5);
    Console.WriteLine(c);
    dynamic a = np.array(new List<float> { 1, 2, 3 });
    dynamic b = np.array(new List<float> { 6, 5, 4 }, Py.kw("dtype", np.int32));
    Console.WriteLine(a.dtype);
    Console.WriteLine(b.dtype);
    Console.WriteLine(a * b);
    Console.ReadKey();
  }
}
```
outputs:
```
1.0  
-0.958924274663
-0.6752620892
float64
int32
[  6.  10.  12.]
```
