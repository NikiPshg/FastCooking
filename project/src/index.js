import React from 'react'
import ReactDOM from 'react-dom/client'
import { Helmet } from 'react-helmet'
import {
    Route,
    Routes,
    BrowserRouter as Router,
} from 'react-router-dom'
import './style.css'
import Frame1 from './views/frame1'
import NotFound from './views/not-found'
import Reg from './views/reg'
import Login from './views/login'
import Meat from './views/meat'
import Ml from "./views/ml";

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
    <>
    <Helmet>
        <title>Fast Cooking</title>
        <link rel="icon" href="star17.svg" type="image/x-icon"/>
        <style>
            @import url('https://fonts.cdnfonts.com/css/days-one');
        </style>
        <script src="https://kit.fontawesome.com/9b617fddaa.js" crossOrigin="anonymous"></script>
    </Helmet>
    <Router>
        <div>
                <Routes>
                    <Route path="/" element={<Frame1/>} />
                    <Route path="/reg" element={<Reg/>} />
                    <Route path="/login" element={<Login/>} />
                    <Route path="/meat" element={<Meat/>} />
                    <Route path="/ml" element={<Ml/>} />
                    <Route path="**"  element={<NotFound/>} />
                </Routes>
        </div>
    </Router>
    </>
);







