import {Component, OnInit} from 'angular2/core';

@Component({
    selector: 'rover-component',
    templateUrl: 'templates/rover_control.component.html',
})

export class RoverControlComponent implements OnInit  { 
  // implement OnInit's `ngOnInit` method
  socket : any;
  ngOnInit() { 
   socket = require('socket.io-client')('/robot');
  }

}
