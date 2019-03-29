import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders, HttpErrorResponse } from '@angular/common/http';
import { environment } from '../../environments/environment';
import {Sprint} from '../models/sprint'
import { AuthService } from './auth.service';

@Injectable({
  providedIn: 'root'
})
export class SprintService {

  constructor(private http: HttpClient, private _auth: AuthService) { }


  listProject() {
    const headers = {
      headers: new HttpHeaders({ 'Content-Type': 'application/json', 'x-access-token': this._auth.getUserToken })
      };
    return this.http.get(environment.API_URL + '/project/', headers)
  }

  listEmployee() {
    const headers = {
      headers: new HttpHeaders({ 'Content-Type': 'application/json', 'x-access-token': this._auth.getUserToken })
      };
    return this.http.get(environment.API_URL + '/employee/', headers)
  }

  listSprints() {
    const headers = {
      headers: new HttpHeaders({ 'Content-Type': 'application/json', 'x-access-token': this._auth.getUserToken })
      };
    return this.http.get(environment.API_URL + '/sprint/', headers)
  }

  getOneSprint(id:number) {
    const headers = {
      headers: new HttpHeaders({ 'Content-Type': 'application/json', 'x-access-token': this._auth.getUserToken })
      };
    return this.http.get(environment.API_URL + '/sprint/'+id+'/', headers)
  }

  listSprint() {
    const headers = {
      headers: new HttpHeaders({ 'Content-Type': 'application/json', 'x-access-token': this._auth.getUserToken })
      };
    return this.http.get(environment.API_URL + '/sprint/', headers)
  }

  createSprint(sprint:Sprint) {
    const headers = {
      headers: new HttpHeaders({ 'Content-Type': 'application/json', 'x-access-token': this._auth.getUserToken })
    };
    const data = {
      name : sprint['name'],
      start_date: sprint['start_date'],
      due_date: sprint['due_date'],
      status: sprint['status'],
      project_id: sprint['project']['id'],
      priority: sprint['priority'],
      employee_id: sprint['employee']['id']
    };
    return this.http.post<any>(environment.API_URL + '/sprint/', data, headers)
  }

  updateSprint(id:string, sprint:Sprint) {
    const headers = {
      headers: new HttpHeaders({ 'Content-Type': 'application/json', 'x-access-token': this._auth.getUserToken })
    };
    const data = {
      name : sprint['name'],
      start_date: sprint['start_date'],
      due_date: sprint['due_date'],
      status: sprint['status'],
      project_id: sprint['project']['id'],
      priority: sprint['priority'],
      employee_id: sprint['employee']['id']
    };
    return this.http.put<any>(environment.API_URL + '/sprint/'+id+'/', data, headers)
  }

  changeSprintStage(id:string, stage:string) {
    const headers = {
      headers: new HttpHeaders({ 'Content-Type': 'application/json', 'x-access-token': this._auth.getUserToken })
    };
    const data = {
      new_stage : stage
    };
    return this.http.put<any>(environment.API_URL + '/sprint/'+id+'/', data, headers)
  }

  deleteSprint(id:string) {
    const headers = {
      headers: new HttpHeaders({ 'Content-Type': 'application/json', 'x-access-token': this._auth.getUserToken })
    };
    return this.http.delete<any>(environment.API_URL + '/sprint/'+id+'/', headers)
  }

  createTaskFromSprint(sprint:Sprint) {
    const headers = {
      headers: new HttpHeaders({ 'Content-Type': 'application/json', 'x-access-token': this._auth.getUserToken })
    };
    const data = {
      name : sprint['name'],
      start_date: sprint['start_date'],
      due_date: sprint['due_date'],
      status: sprint['status'],
      sprint_id: sprint['sprint']['id'],
      priority: sprint['priority'],
      employee_id: sprint['employee']['id']
    };
    return this.http.post<any>(environment.API_URL + '/task/', data, headers)
  }

  addCommentToSprint(id:number, comment:any){
    const headers = {
      headers: new HttpHeaders({ 'Content-Type': 'application/json', 'x-access-token': this._auth.getUserToken })
    };
    const data = {
      comment : comment['comment'],
      employee_id: comment['employee_id']
    };

    return this.http.post<any>(environment.API_URL + '/sprint/tracking/'+id+'/', data, headers)
  }

}
