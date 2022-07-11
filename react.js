import React, { useState, useEffect } from 'react'
import { useDispatch } from 'react-redux'
import axios from 'axios'
import { setCurrentItem } from '../cart/cartSlice'

export function useBeforeFirstRender(f) {
    const [hasRendered, setHasRendered] = useState(false)
    useEffect(() => setHasRendered(true), [hasRendered])
    if (!hasRendered) {
        f()
    }
}

export function AllItems(props) {
    const dispatch = useDispatch()
    const [state, setState] = useState({
        items: [],
    })
    function getDetails(value) {
        dispatch(setCurrentItem(value))
        props.history.push('/itemdetails')
    }
    useBeforeFirstRender(() => {
        axios.get('http://localhost:3001/items/').then(function(response) {
            Object.keys(response.data).forEach(function(item) {
                setState((previousState) => {
                    items: [...previousState.items, response.data[item]]
                })
            })
        })
    })
    return (
        <main>
            <div className="col-05"></div>
            <section id="items-container">
                {state.items.map(function(value) {
                    if (value) {
                        console.log('value ', value)
                    }
                    if (value.category_image) {
                        console.log('value image ', value.item_image)
                    }
                    return (
                        <div id="items-details-container" key={value.slug}>
                            <a onClick={() => getDetails(value)}>
                                <div id="items-img-container">
                                    <img src={value.image} alt=""/>
                                </div>
                                <p>{value.item_name}</p>
                                {/* <p>{value.item_description}</p> */}
                                <p>Price: ${value.price}</p>
                            </a>
                        </div>
                    )
                })}
            </section>
        </main>
    )
}

import { configureStore } from '@reduxjs/toolkit'
import cartReducer from '../features/cart/cartSlice'

export default configureStore({
    reducer: {
        cart: cartReducer,
    }
})

import React, { useState } from 'react'
import { useDispatch } from 'react-redux'
import {
    addCategories
} from './cartSlice'

export function InsertCategories() {
    const dispatch = useDispatch()
    const [state, setState] = useState({
        categoryName: '',
        categoryDescription: '',
        categoryImage: '',
        categorySlug: '',
    })
    const handleChange = (e) => {
        const { name, value } = e.target
        setState((previousState) => ({
            ...previousState,
            [name]: value,
        }))
    }
    function submitForm() {
        dispatch(addCategories(state))
    }
    return (
        <main>
            <div className="col-4"></div>
            <form id="add-category-form" onSubmit={() => dispatch(submitForm())}>
                <h2>Add Category</h2>
                <span>
                    <label htmlFor="category-name">Category Name</label>
                </span>
                <span>
                    <input type="text" id="categoryName" onChange={handleChange} name="categoryName"></input>
                </span>
            </form>
        </main>
    )
}