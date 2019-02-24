import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
	
	public todos: any = [];
	public description: any;
	public label: any;
	public date: any;
  
	constructor() {}

	handleForm() {
		this.todos.push({
			description: this.description,
			label: this.label,
			date: this.date,
			completed: false
		});

		this.description = null;
		this.label = null;
		this.date = '';
	}

	handleCheckbox(todo) {
		todo.completed = !todo.completed;
	}

}
