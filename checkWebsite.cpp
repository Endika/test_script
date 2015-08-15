/*
Author Endika Iglesias <endika2@gmail.com>

How to compile?
Execute this command
g++-4.9 -Wall -std=c++14 checkWebsite.cpp -o checkWebsite
*/
#include <iostream>
#include <string>
#include <ctime>
#include "to.h"

class Website {
public:
  std::string url,
              compare_text;
  Website(std::string url, std::string compare_text);
  bool check_status();
};

/* -- Configuration area -- */
Website webs_lts[2] = {
  //Website("HTTP://WWW.URL TO WEB SITE.COM","TEXT TO COMPARE"),
  Website("endikaiglesias.com","<title>Endika"),
  Website("whitehouse.com","<title>whit")};
/* -- ------------------ -- */

int main(){
    //system("curl endikaiglesias.com");
    To to = To();
    for(int i = 1; i >= 0; i--){
      Website web = webs_lts[i];
      std::cout << to.time_now() << " Check: ";
      if(web.check_status()){
        std::cout << "ON";
      }else{
        std::cout << "OFF";
      }
      std::cout << " -> " << web.url << std::endl;
    }
    return 0;
}

Website::Website(std::string url, std::string compare_text){
  this->url = url;
  this->compare_text = compare_text;
}

bool Website::check_status(){
  bool status;
  std::string text = "",
              command = "curl " + this->url + " -s --insecure  " +
                        "| grep '" + this->compare_text + "'";
  To to = To();
  std::size_t found;
  text = to.cmd(command);
  found = text.find(this->compare_text);
  if(found!=std::string::npos){
    //std::cout << "ON" << std::endl;
    status = true;
  }else{
    //std::cout << "OFF" << std::endl;
    status = false;
  }
  return status;
}
