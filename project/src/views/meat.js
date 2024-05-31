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
                console.log(response.data.image_urls);
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
            <form className="text-form">
                {articles.map((url, index) => (
                    <img key={index} src={url} alt={index}/>
                ))}
            </form>
        </div>
    )
}

export default Meat;