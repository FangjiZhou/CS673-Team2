import { Component, OnInit } from '@angular/core';
import {MatProgressBarModule} from '@angular/material/progress-bar';

@Component({
  selector: 'app-password',
  templateUrl: './password.component.html',
  styleUrls: ['./password.component.css']
})

export class PasswordComponent implements OnInit {
  password = '';
  message = 'Your message goes here';
  messages: string[]=[];
  score:number=0;
  val:number=0;
  color:string='primary';
  bufferValue:number=0;
  strength:string='';

  constructor() { }

  checkPassword(password: string) {
    this.c_length();
    this.c_upperCnt();
    this.c_lowerCnt();
    this.c_numberCnt();
    this.c_metaCnt();
    if(this.messages.length == 0){
      this.messages.push('Password is of good strength');
      this.score+=10;
    }
    this.strength_chk();
  }

  strength_chk():void{
    if (this.score <= 10 )
        {
            this.val = 10; 
            this.bufferValue = 10;  
            this.strength="Very Week";
            this.color='warn';
        }
        else if (this.score > 10 && this.score<=20)
        {
            this.val = 20; 
            this.bufferValue = 20;  
            this.strength="Week";
            this.color='warn';
        }
        else if (this.score > 20 && this.score<=30)
        {
            this.val = 30; 
            this.bufferValue = 30;  
            this.strength="Weak";
            this.color='warn';
        }
        else if (this.score > 30 && this.score<=40)
        {
            this.val = 40; 
            this.bufferValue = 40;  
            this.strength="Medium";
            this.color='accent';
        }
        else {
            this.val = 100; 
            this.bufferValue = 100;  
            this.strength="Strong";
            this.color='primary';
        }

  }

  c_length(): void {
    if ( this.password.length <= 1) {
      this.messages.push('The length of the password is too short');
    }
    else{
      this.score+=10;
    }
  }

  c_numberCnt(): void {
    if ( /\d/.test(this.password) === false) {
      this.messages.push('Password must contain atleast one digit');
    }
    else{
      this.score+=10;
    }

  }

  c_metaCnt(): void {
    if ( /.{8,}/.test(this.password) === false) {
      this.messages.push('Password must contain atleast 8 characters');
    }
    else{
      this.score+=10;
    }

  }

  c_upperCnt(): void {
    if ( /[A-Z]/.test(this.password) === false) {
      this.messages.push('Password must contain atleast one uppercase letter');
    }
    else{
      this.score+=10;
    }

  }

  c_lowerCnt(): void {
    if ( /[a-z]/.test(this.password) === false) {
      this.messages.push('Password must contain atleast one lowercase letter');
    }
    else{
      this.score+=10;
    }
  }

  resetPassword() {
    this.password = '';
    this.messages = [];
    this.score=0;
    this.bufferValue=0;
    this.val=0;
    this.strength='';
    this.color='primary';
  }

  ngOnInit() {
  }

}
