import React from "react";
import axios from "axios";
import {useState, useEffect} from 'react';
import { Helmet } from 'react-helmet';

import './meat.css';


const Meat = (props) => {

    const [articles, setArticles] = useState([]);

    useEffect(() => {
        axios
            .get("http://127.0.0.1:8000/api/v1/urls/")
            .then((response) => {
                setArticles(response.data.image_urls); // Убедитесь, что данные находятся в response.data
                console.log(response.data);
            })
            .catch((error) => {
                console.error("Ошибка при получении данных:", error);
            });

    }, []);

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

            <form className="text-form">
                {articles.map((url, index) => (
                    <img key={index} src={url} alt={index} className="image"/>
                ))}
            </form>
        </div>
    )
}

export default Meat;