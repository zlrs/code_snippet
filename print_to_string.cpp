// using c-style sprintf or snprintf

char buff[100];
snprintf(buff, sizeof(buff), "%s", "Hello");
std::string buffAsStdStr = buff;

// using a string stream

std::ostringstream stringStream;
stringStream << "Hello";
std::string copyOfStr = stringStream.str();
