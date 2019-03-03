import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { AngularFontAwesomeModule } from 'angular-font-awesome';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { NavComponent } from './nav/nav.component';
import { HomeComponent } from './home/home.component';
import { AuthComponent } from './auth/auth.component';
import { IssuesComponent } from './issues/issues.component';
import { SprintsComponent } from './sprints/sprints.component';
import { ChatsComponent } from './chats/chats.component';
import { AdminComponent } from './admin/admin.component';
import { HttpClientModule } from '@angular/common/http';
import { FormsModule } from '@angular/forms';
import { ReactiveFormsModule } from '@angular/forms';
import { AuthGuard } from './guard/auth.guard';
import { DragDropModule } from '@angular/cdk/drag-drop';
import {NgbModule, NgbPaginationModule, NgbAlertModule} from '@ng-bootstrap/ng-bootstrap';

@NgModule({
  declarations: [
    AppComponent,
    NavComponent,
    HomeComponent,
    AuthComponent,
    IssuesComponent,
    SprintsComponent,
    ChatsComponent,
    AdminComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    FormsModule,
    ReactiveFormsModule,
    DragDropModule,
    AngularFontAwesomeModule,
    NgbModule,
    NgbPaginationModule, 
    NgbAlertModule
  ],
  providers: [AuthGuard],
  bootstrap: [AppComponent]
})
export class AppModule { }
