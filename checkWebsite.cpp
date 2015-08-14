/*
Author Endika Iglesias <endika2@gmail.com>

How to compile?
Execute this command
g++-4.9 -Wall -std=c++14 checkWebsite.cpp -o checkWebsite
*/
#include <iostream>
#include <string>
#include <ctime>

std::string time_now();

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
    for(int i = 1; i >= 0; i--){
      Website web = webs_lts[i];
      std::cout << time_now() << " Check: ";
      if(web.check_status()){
        std::cout << "ON";
      }else{
        std::cout << "OFF";
      }
      std::cout << " -> " << web.url << std::endl;
    }
    return 0;
}

std::string time_now(){
  time_t rawtime;
  struct tm * timeinfo;
  char buffer[80];
  time (&rawtime);
  timeinfo = localtime(&rawtime);
  strftime(buffer, 80, "%d-%m-%Y %I:%M:%S", timeinfo);
  std::string str(buffer);
  return str;
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
  std::size_t found;
  FILE* fp;
  char result [1000000];
  fp = popen(command.c_str(),"r");
  fread(result,1,sizeof(result),fp);
  fclose (fp);
  for(int i=0;i<1000000;i++){
      text += result[i];
  }
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

