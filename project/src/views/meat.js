import React from "react";
import axios from "axios";
import {useState, useEffect} from 'react';
import { Helmet } from 'react-helmet';

import TextFromServer from '../TextFromServer';
import ImgFromServer from "../ImgFromServer";

import './meat.css';


const Meat = (props) => {

    return (
        <div className="frame1-container">
            <Helmet>
                <title>Fast Cooking</title>
                <link rel="icon" href="star17.svg" type="image/x-icon"/>
                <style>
                    @import url('https://fonts.cdnfonts.com/css/days-one');
                </style>
            </Helmet>

            <div className="header">
                <span className="frame1-text54">
                <span className="frame1-text55">Fast</span>
                <br></br>
                <span className="frame1-text57"></span>
                <span>Cooking</span>
            </span>
                <img
                    src="star17.svg"
                    alt="Star16051"
                    className="frame1-star1"
                />
                <input
                    className="frame1-rectangle131"
                    type="search"
                    placeholder="Выбрать рецепт"
                />
                <img
                    src="Lupa.png"
                    alt="Ellipse46051"
                    className="frame1-ellipse41"
                />
            </div>
            <div className="cool">
            <ImgFromServer />
            <TextFromServer />
            </div>
        </div>
    )
}

export default Meat;