//#include <iostream>
//#include "Compiler107.h"
//
//using namespace std;
//
//int main(){
//    string path = "D:\\CodeStudy\\compiler\\test1.txt";
//    Compiler107 c;
//    c.init(path);
//    cout<<"initialized"<<endl;
//    c.lex_ana();
//    cout<<"lexical_analysis finished"<<endl;
//    c.parse();
////    c.optimize();
////    c.output();
//}

#include <iostream>
#include "Compiler107.h"

using namespace std;

int main(){
    string path;
//    cout << "Please input file path: " << endl;
    cin >> path;
//    path = "D:\\CodeStudy\\compiler\\test2.txt";
    Compiler107 c;
    c.init(path);
    //cout << "initialized" << endl;
    cout<<"lexical_analysis: "<<endl;
    c.lex_ana();
    cout<<"--------"<<endl;
    cout<<"parse processing: "<<endl;
    c.parse();
    c.optimize();
    c.output();
}

//D:\\CodeStudy\\compiler\\test1.txt
