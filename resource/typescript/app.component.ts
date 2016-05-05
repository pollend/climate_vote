import {Component} from 'angular2/core';
import { RouteConfig, ROUTER_DIRECTIVES, ROUTER_PROVIDERS,AsyncRoute} from 'angular2/router';

import {HomeComponent} from './home.component';
import {MembersComponent} from './members.component';
import {ContactsComponent} from './contacts.component';
import {RoverComponent} from './rover.component';

@Component({
    selector: 'my-app',
    templateUrl: 'templates/app.component.html',
    directives: [ROUTER_DIRECTIVES],
    providers: [ROUTER_PROVIDERS]
})


@RouteConfig([
	{
		path:"/Home",
		name:"Home",
		useAsDefault : true,
		component: HomeComponent
	},
	{
		path: "/Members",
		name: "Members",
		component: MembersComponent
	},
	{
		path: "/Contacts",
		name: "Contacts",
		component: ContactsComponent
	},
	{
		path: "/Rover",
		name: "Rover",
		component: RoverComponent
	}
])

export class AppComponent { 
	
  //expand with mobile application mode
  expand()
  {
    $(".navigation nav").each(function(index)
    {
      if($(this).hasClass("show"))
        $(this).removeClass("show");
      else
        $(this).addClass("show");

    });
  }
}

