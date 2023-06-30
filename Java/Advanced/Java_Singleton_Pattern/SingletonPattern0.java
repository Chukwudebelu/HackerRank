//!/bin/java
import java.io.*;
import java.util.*;
import java.text.*;
import java.util.regex.*;
import java.lang.reflect.*;


class Singleton {
  private static Singleton instance = null;
  
  private Singleton() {}
  
  public String str;
  
  public static Singleton getSingleInstance() {
    if (instance == null) {
      instance = new Singleton();
    }
    return instance;
  }
}
