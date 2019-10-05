int x_initial;
int y_initial;
int z_initial;

void setup() 
{ 
Serial.begin(9600);

x_initial=analogRead(0);
y_initial=analogRead(1);
z_initial=analogRead(2);
}

void loop() 
{ 
int x_after_retrieval;
int y_after_retrieval;
int z_after_retrieval;

x_after_retrieval=analogRead(0);
y_after_retrieval=analogRead(1);
z_after_retrieval=analogRead(2);

x_after_retrieval-=x_initial;
y_after_retrieval-=y_initial;
z_after_retrieval-=z_initial;

if(y_after_retrieval<-20)
{
  Serial.print("u");
}
delay(100);
if(y_after_retrieval>20)
{
  Serial.print("d");
}
delay(100);
if(z_after_retrieval<20)
{
  Serial.print("l");
}
delay(100);
if(z_after_retrieval<-20)
{
  Serial.print("r");
}
delay(100);
if(y_after_retrieval<20)
{
  Serial.print("a");
}
delay(100);
if(y_after_retrieval<-20)
{
  Serial.print("b");
}
delay(100);
}
