import { Component, OnInit } from '@angular/core';
import {AuthService} from '../services/auth.service'
import { Router, ActivatedRoute } from '@angular/router'
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { first } from 'rxjs/operators';

@Component({
  selector: 'app-auth',
  templateUrl: './auth.component.html',
  styleUrls: ['./auth.component.scss']
})
export class AuthComponent implements OnInit {
  
  loginForm: FormGroup;
  loading = false;
  submitted = false;
  returnUrl: string;
  error = '';

  constructor(private formBuilder: FormBuilder,
              private route: ActivatedRoute,
              private router: Router,
              private _auth: AuthService, 
              private _router: Router) { 
                // redirect to home if already logged in
                  if (this._auth.isAuthenticated) { 
                    //this.router.navigate(['/issues']);
                     console.log('already loogedIn')
                }
              }

  ngOnInit() {
    this.loginForm = this.formBuilder.group({
      username: ['', Validators.required],
      password: ['', Validators.required]
  });

  // get return url from route parameters or default to '/'
  this.returnUrl = this.route.snapshot.queryParams['returnUrl'] || '/issues';
  }

  // convenience getter for easy access to form fields
  get f() { return this.loginForm.controls; }

  onSubmit() {
      this.submitted = true;
      // stop here if form is invalid
      if (this.loginForm.invalid) {
          return;
      }

      this.loading = true;
      this._auth.loginUser(this.f.username.value, this.f.password.value).subscribe(
          data => {
            localStorage.setItem('currentUser', JSON.stringify(data));
            this.router.navigate([this.returnUrl]);
          },
          error => {
            this.error = error;
            this.loading = false;
      });
  }

  

}
