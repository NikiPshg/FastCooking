import React from 'react'
import ReactDOM from 'react-dom'
import {
  BrowserRouter as Router,
  Route,
  Switch,
  Redirect,
} from 'react-router-dom'

import './style.css'
import Frame1 from './views/frame1'
import NotFound from './views/not-found'
import Reg from './views/reg'


const App = () => {
  return (

  <Router>
    <Switch>
      <Route component={Frame1} exact path="/" className={''}/>
      <Route component={Reg} exact path="/reg" />
      <Route component={NotFound} exact path="**" />
      <Redirect to="**" />
    </Switch>
  </Router>
  )
}

ReactDOM.render(<App />, document.getElementById('app'))

