import React from 'react'

import { Helmet } from 'react-helmet'

import './login.css'

const Login = (props) => {
    return (
        <div className="frame1-container_log">
            <Helmet>
                <title>Fast Cooking</title>
                <link rel="icon" href="star17.svg" type="image/x-icon"/>
                <style>
                    @import url('https://fonts.cdnfonts.com/css/days-one');
                </style>
            </Helmet>
            <form className="login-form">
                <h1>Вход</h1>

                <div className="text2">Почта/Логин</div>
                <div className="text_log">
                    <input type="text"/>
                </div>

                <div className="text3">Пароль</div>
                <div className="text_log">
                    <input type="password"/>
                </div>

                <input type="submit" className="button_log" value="Войти"/>

                <div className="bottom-text_log">
                    Нет аккаунта? <a href="reg">Зарегистрироваться</a>
                </div>

            </form>
        </div>
    )
}

export default Login
