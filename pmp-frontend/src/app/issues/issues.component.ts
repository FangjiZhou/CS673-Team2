import { Component, OnInit, ElementRef } from '@angular/core';
import {CdkDragDrop, moveItemInArray, transferArrayItem} from '@angular/cdk/drag-drop';
import {NgbModal, ModalDismissReasons} from '@ng-bootstrap/ng-bootstrap';
import {Issue} from '../models/issue'
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import {IssuetrackerService} from '../services/issuetracker.service'


@Component({
  selector: 'app-issues',
  templateUrl: './issues.component.html',
  styleUrls: ['./issues.component.scss']
})
export class IssuesComponent implements OnInit {

  closeResult: string;

  newIssueForm: FormGroup;
  loading = false;
  submitted = false;
  returnUrl: string;
  error = '';
  project_list=[]
  employee_list=[]
  issue_list=[]

  // init the list to classify issues
  done =[]
  inputqueue = [];
  requirementsgathering = [];
  workinprogress = [];
  qualityassurance = [];
  useracceptance = [];

  constructor(private modalService: NgbModal, private formBuilder: FormBuilder, private eleRef: ElementRef, private issueTracker: IssuetrackerService) { }
  
  ngOnInit() {
    this.newIssueForm = this.formBuilder.group({
      name: ['', Validators.required],
      start_date: ['', Validators.required],
      due_date: ['', Validators.required],
      priority: ['', Validators.required],
      project_id: ['', Validators.required],
      employee_id: ['', Validators.required]
  });
  // init the globals arrays of list
  this.issueTracker.listProject().subscribe(data => {
    this.project_list = data['projects']
  });

  this.issueTracker.listEmployee().subscribe(data => {
    this.employee_list = data['employees']
  });

  this.issueTracker.listIssues().subscribe(data => {
    this.issue_list = data['issues']

    //filter for each arrray
    this.inputqueue = this.issue_list.filter(issue => issue['status']=='Input Queue');
    this.requirementsgathering = this.issue_list.filter(issue => issue['status']=='Requirements Gathering');
    this.workinprogress = this.issue_list.filter(issue => issue['status']=='Work In Progress');
    this.qualityassurance = this.issue_list.filter(issue => issue['status']=='Quality Assurance');
    this.useracceptance = this.issue_list.filter(issue => issue['status']=='User Acceptance');
    this.done = this.issue_list.filter(issue => issue['status']=='Done');
  });

  }
  // convenience getter for easy access to form fields
  get i() { return this.newIssueForm.controls; }

  // create new issue
  onSubmitNewIssue(modal) {
    this.submitted = true;
    // stop here if form is invalid
    if (this.newIssueForm.invalid) {
        return;
    }
    // the issue is valid and we can push it to the rest api
    var new_issue:Issue = {id: null, dateAdded: new Date().toString(), 
      name : this.i.name.value, start_date : this.i.start_date.value['year']+"-"+this.i.start_date.value['month']+"-"+this.i.start_date.value['day']+" 00:00:00",
      due_date : this.i.due_date.value['year']+"-"+this.i.due_date.value['month']+"-"+this.i.due_date.value['day']+" 23:59:59", status : "Input Queue",
      priority : this.i.priority.value, project : JSON.parse(this.i.project_id.value), employee : JSON.parse(this.i.employee_id.value)}
    
    // call the service to create the issue: 
    this.issueTracker.createIssue(new_issue).subscribe(
      data => {
        var id_ = data['id']
        new_issue['id']=id_
        console.log('issue created');
        this.issueTracker.getOneIssue(id_).subscribe(data => {
          this.inputqueue.push(data['issue']);
        });
        this.newIssueForm.reset();
        modal.dismiss('Submitting the form');
        this.submitted = false;
      },
      error => {
        this.error = error;
        console.log('fail to create issue');
        console.log(new_issue)
  });

}

  addItem(list: string, todo: Issue) {
    if(todo == null){
      return;
    }
    else{
      var new_issue = todo;
    }
    if (list === 'inputqueue') {
      this.inputqueue.push(new_issue);
    } else {
      this.workinprogress.push(new_issue);
    }
  }


  drop(event: CdkDragDrop<Issue[]>) {
    // first check if it was moved within the same list or moved to a different list
    if (event.previousContainer === event.container) {
      // change the items index if it was moved within the same list
      console.log(event.item.element)
      moveItemInArray(event.container.data, event.previousIndex, event.currentIndex);
    } else {      
      var issue_id = event.item.element.nativeElement.id
      var stage_name = event.container.element.nativeElement.id

      // update the stage of the issue
      // call the service to create the issue: 
    this.issueTracker.changeIssueStage(issue_id, stage_name).subscribe(
      data => {
        // remove item from the previous list and add it to the new array
        transferArrayItem(event.previousContainer.data, event.container.data, event.previousIndex, event.currentIndex);
        console.log('issue stage updated');
      },
      error => {
        console.log(error)
  });
    }
  }

  open(content) {
    this.modalService.open(content, {ariaLabelledBy: 'modal-basic-title'}).result.then((result) => {
      this.closeResult = `Closed with: ${result}`;
    }, (reason) => {
      this.closeResult = `Dismissed ${this.getDismissReason(reason)}`;
    });
  }

  private getDismissReason(reason: any): string {
    if (reason === ModalDismissReasons.ESC) {
      return 'by pressing ESC';
    } else if (reason === ModalDismissReasons.BACKDROP_CLICK) {
      return 'by clicking on a backdrop';
    } else {
      return  `with: ${reason}`;
    }
  }

}
