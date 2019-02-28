import { Component, OnInit } from '@angular/core';
import {CdkDragDrop, moveItemInArray, transferArrayItem} from '@angular/cdk/drag-drop';
import {Issue} from '../models/issue'

@Component({
  selector: 'app-issues',
  templateUrl: './issues.component.html',
  styleUrls: ['./issues.component.scss']
})
export class IssuesComponent implements OnInit {

  constructor() { }
  
  
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
  
  ngOnInit() {
  }

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
      moveItemInArray(event.container.data, event.previousIndex, event.currentIndex);
    } else {
      // remove item from the previous list and add it to the new array
      transferArrayItem(event.previousContainer.data, event.container.data, event.previousIndex, event.currentIndex);
      console.log(event.item.element.nativeElement.id)
      console.log(event.container.element.nativeElement.id)
    }
  }

}
