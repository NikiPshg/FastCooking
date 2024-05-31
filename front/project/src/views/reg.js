import React from 'react'

import { Helmet } from 'react-helmet'

import './reg.css'


const Reg = (props) => {
    return (
        <div className="frame1-container">
            <Helmet>
                <title>Fast Cooking</title>
                <link rel="icon" href="star17.svg" type="image/x-icon"/>
                <style>
                    @import url('https://fonts.cdnfonts.com/css/days-one');
                </style>
            </Helmet>
            <form className="reg-form">
            <h1>Регистрация</h1>
                <div className="text1">Логин</div>
                <div className="text">
                    <input type="text"/>
                </div>
                <div className="text1">Почта</div>
                <div className="text">
                    <input type="email"/>
                </div>
                <div className="text1">Пароль</div>
                <div className="text">
                    <input type="password"/>
                </div>
                <div className="text1">Подтвердите пароль</div>
                <div className="text">
                    <input type="password"/>
                </div>

                <input type="submit" className="button" value="Зарегистрироваться"/>

                <div className="bottom-text">
                    Есть аккаунт? <a href="login">Войти</a>
                </div>

            </form>
        </div>
    )
}

export default Reg
