#include <iostream>
#include <string>
#include <ctime>

class To{
public:
  std::string time_now();
  std::string cmd(std::string command);
};

std::string To::time_now(){
  time_t rawtime;
  struct tm * timeinfo;
  char buffer[80];
  time (&rawtime);
  timeinfo = localtime(&rawtime);
  strftime(buffer, 80, "%d-%m-%Y %I:%M:%S", timeinfo);
  std::string str(buffer);
  return str;
}

std::string To::cmd(std::string command){
  std::string text = "";
  FILE* fp;
  char result [1000000];
  fp = popen(command.c_str(), "r");
  fread(result, 1, sizeof(result), fp);
  fclose(fp);
  for(int i=0; i < 1000000; i++){
      text += result[i];
  }
  return text;
}
