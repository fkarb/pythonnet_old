// ==========================================================================
// This software is subject to the provisions of the Zope Public License,
// Version 2.0 (ZPL).  A copy of the ZPL should accompany this distribution.
// THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
// WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
// WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
// FOR A PARTICULAR PURPOSE.
// ==========================================================================

using System;
using System.Collections;
using System.Windows.Forms;

namespace Python.Test {

    //========================================================================
    // Supports CLR generics unit tests.
    //========================================================================
    
    public class GenericWrapper<T> {
        public T value;

        public GenericWrapper(T value) {
            this.value = value;
        }
    }

    public class GenericTypeDefinition<T, U> {
        public T value1;
        public U value2;

        public GenericTypeDefinition(T arg1, U arg2) {
            this.value1 = arg1;
            this.value2 = arg2;
        }
    }

    public class DerivedFromOpenGeneric<V, W> : 
                 GenericTypeDefinition<int, V> {

        public W value3;

        public DerivedFromOpenGeneric(int arg1, V arg2, W arg3) : 
               base(arg1, arg2) {
            this.value3 = arg3;
        }
    }


    public class GenericNameTest1 {
        public static int value = 0;
    }

    public class GenericNameTest1<T> {
        public static int value = 1;
    }

    public class GenericNameTest1<T,U> {
        public static int value = 2;
    }

    public class GenericNameTest2<T> {
        public static int value = 1;
    }

    public class GenericNameTest2<T,U> {
        public static int value = 2;
    }


    public class GenericMethodTest<T> {

        public GenericMethodTest() {}

        public int Overloaded() {
            return 1;
        }

        public T Overloaded(T arg) {
            return arg;
        }

        public Q Overloaded<Q>(Q arg) {
            return arg;
        }

        public U Overloaded<Q, U>(Q arg1, U arg2) {
            return arg2;
        }

        public string Overloaded<Q>(int arg1, int arg2, string arg3) {
            return arg3;
        }

    }

    public class GenericStaticMethodTest<T> {

        public GenericStaticMethodTest() {}

        public static int Overloaded() {
            return 1;
        }

        public static T Overloaded(T arg) {
            return arg;
        }

        public static Q Overloaded<Q>(Q arg) {
            return arg;
        }

        public static U Overloaded<Q, U>(Q arg1, U arg2) {
            return arg2;
        }

        public static string Overloaded<Q>(int arg1, int arg2, string arg3) {
            return arg3;
        }

    }


}
