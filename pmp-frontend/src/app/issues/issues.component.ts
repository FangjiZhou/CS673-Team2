import { Component, OnInit, ElementRef } from '@angular/core';
import {CdkDragDrop, moveItemInArray, transferArrayItem} from '@angular/cdk/drag-drop';
import {NgbModal, ModalDismissReasons} from '@ng-bootstrap/ng-bootstrap';
import {Issue} from '../models/issue'
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { element } from '@angular/core/src/render3';

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

  constructor(private modalService: NgbModal, private formBuilder: FormBuilder, private eleRef: ElementRef) { }
  
  ngOnInit() {
    this.newIssueForm = this.formBuilder.group({
      name: ['', Validators.required],
      start_date: ['', Validators.required],
      due_date: ['', Validators.required],
      project_id: ['', Validators.required],
      employee_id: ['', Validators.required]
  });
  }

  resetNewIssue(){
    this.newIssueForm = this.formBuilder.group({
      name: ['', Validators.required],
      start_date: ['', Validators.required],
      due_date: ['', Validators.required],
      project_id: ['', Validators.required],
      employee_id: ['', Validators.required]
   });
  }
  new_issue = {
    "name": "",
    "start_date":"",
    "due_date":"",
    "status": "",
    "project_id": null,
    "employee_id":null
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

    console.log('issue to create');
    this.newIssueForm.reset();
    modal.dismiss('Submitting the form');
    this.submitted = false;
}

  public inputqueue: Issue[] = [
    {id:1, title: 'Get to work', dateAdded: new Date().toString() },
    {id:2, title: 'Pick up groceries', dateAdded: new Date().toString() },
    {id:3, title: 'Go home', dateAdded: new Date().toString() },
    {id:4, title: 'Fall asleep', dateAdded: new Date().toString() }
  ];

  public requirementsgathering: Issue[] = [
    {id:7, title: 'Take a shower', dateAdded: new Date().toString() },
    {id:8, title: 'Check e-mail', dateAdded: new Date().toString() },
    {id:9, title: 'Walk dog', dateAdded: new Date().toString() }
    ];

  public workinprogress: Issue[] = [];

  public qualityassurance: Issue[] = [];

  public useracceptance: Issue[] = [];

  public done: Issue[] = [
    {id:5, title: 'Get up', dateAdded: new Date().toString() },
    {id:6, title: 'Brush teeth', dateAdded: new Date().toString() }
  ];

  addItem(list: string, todo: string) {
    if (list === 'inputqueue') {
      this.inputqueue.push({id:21, title: todo, dateAdded: new Date().toString() });
    } else {
      this.workinprogress.push({id:22, title: todo, dateAdded: new Date().toString() });
    }
  }


  drop(event: CdkDragDrop<Issue[]>) {
    // first check if it was moved within the same list or moved to a different list
    if (event.previousContainer === event.container) {
      // change the items index if it was moved within the same list
      console.log(event.item.element)
      moveItemInArray(event.container.data, event.previousIndex, event.currentIndex);
    } else {
      // remove item from the previous list and add it to the new array
      transferArrayItem(event.previousContainer.data, event.container.data, event.previousIndex, event.currentIndex);
      console.log(event.item.element.nativeElement.id)
      console.log(event.container.element.nativeElement.id)
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
