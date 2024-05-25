import React from "react";

import styles from "./BigPlus.module.css"

//https://react-bootstrap.github.io/docs/components/dropdowns#customization

const BigPlus = React.forwardRef(
    function BigPlus({ children, onClick }, ref) {

        const buttonStyle = "btn btn-primary btn-lg " + styles.adderButton
        const iconStyle = "bi bi-plus " + styles.icon

        return (
            <>
                <a type="button" ref={ref} className={buttonStyle}
                    onClick={(e) => {
                        e.preventDefault();
                        onClick(e);
                    }}>
                    {children}
                    <i className={iconStyle}></i>
                </a>
            </>
        )
    }
);

export default BigPlus;