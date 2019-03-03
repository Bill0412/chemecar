#define IN1 4
#define IN2 3
#define ENA 2
#define IN3 6
#define IN4 5
#define ENB 7

#define TURN_SPEED 100
int s[8];
double k,vl,vr,kl,kr;
bool isTurning;
bool isPassingLine;
bool isToFollowLine;
bool isFirstTime;

void LeftMotor(int speed);
void RightMotor(int speed);
void TurnLeft(int speed);
void TurnRight(int speed);
void FollowLine();

void setup()
{
  pinMode(IN1, OUTPUT);
  pinMode(IN2, OUTPUT);
  pinMode(IN3, OUTPUT);
  pinMode(IN4, OUTPUT);
  pinMode(A0, INPUT);
  pinMode(A1, INPUT);
  pinMode(A2, INPUT);
  pinMode(A3, INPUT);
  pinMode(A4, INPUT);
  pinMode(A5, INPUT);
  pinMode(A6, INPUT);
  pinMode(A7, INPUT);
  Serial.begin(9600);
  kl=0.02;
  kr=-0.02;
  vl=200;
  vr=165;
  isTurning = false;
  isPassingLine = false;
  isToFollowLine = true;
}

void loop()  
{
  // In contest white: 0. black: 1 or 1024
  // white-black conversion, only used in test
  // i.e., white: 1, black 0
  s[0]=1024-analogRead(A2);
  s[1]=1024-analogRead(A3);
  s[2]=1024-analogRead(A4);
  s[3]=1024-analogRead(A5);
  s[4]=1024-analogRead(A0);
  s[5]=1024-analogRead(A1);
  s[6]=1024-analogRead(A6);
  s[7]=1024-analogRead(A7);

  // filter out environment light: convert to digital
  for(int i = 0; i < 8; i++){
   if(s[i]>500) {
    // detects white area
    s[i] = 1024;
   } else {
    // detects black area
    s[i] = 0;  
   }
  }
  if ( Serial.available())
    {
      if('f' == Serial.read())
        Serial.println("Hello Raspberry,I am Arduino.");
  if(!s[6] && !s[4]) {
    isToFollowLine = false;
    isPassingLine = true;
  }
  
  if(isToFollowLine){
    FollowLine();
  } else {
    //TurnLeft(TURN_SPEED);
    TurnRight(TURN_SPEED);
    // if is turning and front sensors pass black totally
      isTurning=true;
      // if s[3] detects black, it leaves the black line.
      if(!s[3]) {
       // front sensors detect white area
      isTurning = true;
      isPassingLine = false;
    }

     if(isTurning) {
      // if one of the front sensors  dectects black, switch back to follow line, a turning succeeds
      
      //isToFollowLine = isToFollowLine || !s[i];
      if(!s[0]) {
        isToFollowLine = true;
        isTurning = isPassingLine = false;
      }
/*
      if(isToFollowLine) {
        // FollowLine();
       isTurning = isPassingLine = false;
       delay(2000);
      }*/
     }
  }        
     }
    // if one of the side sensors detects the crossing line(black in test, white in contest)

}

void LeftMotor(int speed)
{
  if(speed>255)speed=255;
  
  if(speed > 0)
  {
    digitalWrite(IN1, HIGH);
    digitalWrite(IN2, LOW);
    analogWrite(ENA, speed);
  }
  
  else 
  {
    digitalWrite(IN1, LOW);
    digitalWrite(IN2,HIGH );
    analogWrite(ENA, -speed);
  }
/*  if(speed < 0)
 *   else
  {
    digitalWrite(IN1, LOW);
    digitalWrite(IN2, LOW);
    analogWrite(ENA, 0);
  }*/
}

void RightMotor(int speed)
{
  if(speed>255)speed=255;
  if(speed > 0)
  {
    digitalWrite(IN3, HIGH);
    digitalWrite(IN4, LOW);
    analogWrite(ENB, speed);
  }
  else 
  {
    digitalWrite(IN3, LOW);
    digitalWrite(IN4, HIGH);
    analogWrite(ENB, -speed);
  }/*
  if(speed < 0)
  else
  {
    digitalWrite(IN3, LOW);
    digitalWrite(IN4, LOW);
    analogWrite(ENB, 0);
  }*/
}

void TurnLeft(int speed) 
{
  LeftMotor(-speed);
   RightMotor(speed);
}

void TurnRight(int speed) 
{
  TurnLeft(-speed);
}

void FollowLine()
{
  int x=(-3)*s[0]+(-1)*s[1]+1*s[2]+3*s[3];
  double leftSpeed = vl+kl*x;
  double rightSpeed = vr+kr*x;

  LeftMotor(leftSpeed);
  RightMotor(rightSpeed);
}
