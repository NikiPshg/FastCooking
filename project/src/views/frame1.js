import './frame1.css';
import {useState, useEffect} from 'react';
import axios from 'axios';
const src = "https://content.guardianapis.com/search?q=debate&tag=politics/politics&from-date=2014-01-01&api-key=test"
function Frame1() {

    const [selectedFile, setSelectedFile] = useState(null);

    const handleFileChange = (event) => {
        setSelectedFile(event.target.files[0]);
    };

    const handleUpload = () => {
        const formData = new FormData();
        formData.append('file', selectedFile);

        axios.put('http://127.0.0.1:8000/api/v1/media/recipe_images/', formData)
            .then(response => {
                console.log('File uploaded successfully:', response.data);
            })
            .catch(error => {
                console.error('Error uploading file:', error);
            });
    };
    return (
        <div className="frame1-container">
            <div className="frame1-frame1">
                <img src="/fluentmdl2eatdrink6056-2zx.svg"
                     alt="fluentmdl2eatdrink6056"
                     className="frame1-fluentmdl2eatdrink"
                />
                <span className="frame1-text">
          <span>Рецепты FastCooking</span>
        </span>
                <span className="frame1-text02">
            Наш сайт - ваш личный ассистент в кулинарии!
        </span>
                <span className="frame1-text06">
          <span>Просто сфотографируйте продукты, которые у вас есть,</span>
          <br></br>
          <span>и он мгновенно подберет для вас самые вкусные</span>
          <br></br>
          <span>и оригинальные рецепты.</span>
          <br></br>
          <span>Наслаждайтесь новыми кулинарными открытиями</span>
          <br></br>
          <span>с нашим умным помощником!</span>
        </span>
                <span className="frame1-text16">
          <span>Отзывы наших клиентов</span>
        </span>
                <img
                    src="/ellipse16057-jeks-200h.png"
                    alt="Ellipse16057"
                    className="frame1-ellipse1"
                />
                <span className="frame1-text18">
          <span>Матвей Лень</span>
        </span>
                <img
                    src="/rectangle56057-43ju-400h.png"
                    alt="Rectangle56057"
                    className="frame1-rectangle5"
                />
                <span className="frame1-text20">
          <span>Сайт очень удобный, подобрал своей</span>
          <br></br>
          <span>
            бабушке рецепты, а то надоело постоянно
            <span
                dangerouslySetInnerHTML={{
                    __html: ' ',
                }}
            />
          </span>
          <br></br>
          <span>
            есть подгоревший омлет,
            <span
                dangerouslySetInnerHTML={{
                    __html: ' ',
                }}
            />
          </span>
          <br></br>
          <span>щас вот питаюсь как барон.</span>
          <br></br>
          <span>Спасибо!</span>
        </span>
                <div className="stars1">
                    <img
                        src="/star13.png"
                        className="stars1-star1"
                    />
                    <img
                        src="/star13.png"
                        className="stars1-star2"
                    />
                    <img
                        src="/star13.png"
                        className="stars1-star3"
                    />
                    <img
                        src="/star13.png"
                        className="stars1-star4"
                    />
                    <img
                        src="/star13.png"
                        className="stars1-star5"
                    />
                </div>

                <div className="stars2">
                    <img
                        src="/star13.png"
                        className="stars2-star1"
                    />
                    <img
                        src="/star13.png"
                        className="stars2-star2"
                    />
                    <img
                        src="/star13.png"
                        className="stars2-star3"
                    />
                    <img
                        src="/star13.png"
                        className="stars2-star4"
                    />
                    <img
                        src="/star13.png"
                        className="stars2-star5"
                    />
                </div>
                <img
                    src="/vector16058-m0gc.svg"
                    alt="Vector16058"
                    className="frame1-vector1"
                />
                <img
                    src="/rectangle66058-xxw8-400h.png"
                    alt="Rectangle66058"
                    className="frame1-rectangle6"
                />
                <span className="frame1-text30">
          <span>
            Отличный сайт для тех, кто не любит
            <span
                dangerouslySetInnerHTML={{
                    __html: ' ',
                }}
            />
          </span>
          <br></br>
          <span>тратить много времени на поиск рецептов!</span>
          <br></br>
          <span>
            Просто загрузи фото доступных
            <span
                dangerouslySetInnerHTML={{
                    __html: ' ',
                }}
            />
          </span>
          <br></br>
          <span>ингредиентов, и сайт подберет для вас</span>
          <br></br>
          <span>подходящие рецепты. Удобно и быстро</span>
        </span>
                <span className="frame1-text40">
          <span></span>
          <br></br>
          <span></span>
        </span>

                <img
                    src="/vector26059-fang.svg"
                    alt="Vector26059"
                    className="frame1-vector2"
                />
                <img
                    src="/ellipse26059-k1d-200h.png"
                    alt="Ellipse26059"
                    className="frame1-ellipse2"
                />
                <span className="frame1-text44">
          <span>Никифорова Екатерина</span>
        </span>
                <a href="http://localhost:3000/meat">
                    <img
                        src="/rectangle166059-9d09-500h.png"
                        alt="Rectangle166059"
                        className="frame1-rectangle16"
                    />
                </a>
                <span className="frame1-text46">
          <span>Мясо</span>
        </span>
                <img
                    src="/rectangle17button6059-e5ne-500h.png"
                    alt="Rectangle17button6059"
                    className="frame1-rectangle17button"
                />

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
                        className="frame1-rectangle13"
                        type="search"
                        placeholder="Выбрать рецепт"
                    />
                    <a className="frame1-text48" href="login">
                        Войти
                    </a>
                    <a className="frame1-text50" href="reg">
                        Регистрация
                    </a>
                    <img
                        src="Lupa.png"
                        alt="Ellipse46051"
                        className="frame1-ellipse4"
                    />
                    <a className="frame1-text59" href="#About1">
                        О сайте
                    </a>
                </div>

                <img
                    src="/line16051-ppyd.svg"
                    alt="Line16051"
                    className="frame1-line1"
                />


                <img
                    src="/rectangle196051-kprf-200h.png"
                    alt="Rectangle196051"
                    className="frame1-rectangle19"
                />
                <ul className="widgets">
                    <a href="tg" className="fa fa-telegram"></a>
                    <a href="vk" className="fa fa-vk"></a>
                </ul>
                <img
                    src="/biccircle6051-pxnv.svg"
                    alt="biccircle6051"
                    className="frame1-biccircle"
                />
                <span className="frame1-text61">
          <span>FastCooking, 2024</span>
        </span>
                <span className="frame1-text63">
          <span>
            Если возникли какие-то
            <span
                dangerouslySetInnerHTML={{
                    __html: ' ',
                }}
            />
          </span>
          <br></br>
          <span>проблемы, свяжитесь с нами</span>
        </span>
                <span className="frame1-text67">
          <span>Вверх</span>
        </span>
                <a className="link" href="#">
                </a>
                <img
                    src="arrow.png"
                    className="arrow"
                />
                <span className="frame1-text69">
                <span className="frame1-text691">Здоровое</span>
                <span className="frame1-text692">питание</span>
            </span>
                <input
                    type="file"
                    className="frame1-rectangle15"
                    onChange={handleFileChange}
                />
                <button onClick={handleUpload}>Upload</button>
                <span className="frame1-text71">
          <span>Загрузи фото продуктов</span>
          <br></br>
          <span>и получи рецепт мечты!</span>
        </span>
                <img
                    src="/vector6051-akij.svg"
                    alt="Vector6051"
                    className="frame1-vector"
                />
                <div className="about" id="About1"></div>
            </div>
        </div>
    )
}

export default Frame1

