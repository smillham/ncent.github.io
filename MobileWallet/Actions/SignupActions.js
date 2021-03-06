import firebase from 'firebase';
import {USER_UPDATE, CREATE_USER, CREATE_USER_SUCCESS, CREATE_USER_FAIL} from './types';
import {Actions} from 'react-native-router-flux';
import ncentSDK from 'ncent-sdk-public';

const ncentSDKInstance = new ncentSDK();

export const userUpdate = ({prop, value}) => {
	return {
		type: USER_UPDATE,
		payload: { prop, value }
	};
};

export const createUser = ({first, last, email, username, phone, password, confirm}) => {
	return (dispatch) => {
		dispatch({type: CREATE_USER});
		// check if wallet address exists, return error if so
		let new_user = undefined;
		firebase.auth().createUserWithEmailAndPassword(email, password)
		.then(user => {
			// create wallet, get address, pk
			new_user = user;
			console.log("here");
			firebase.database().ref(`/users/${user.user.uid}/information`)
			.push({first, last, email, username, phone});
			console.log("and here");
					
		})
		.then( () => {
	 		dispatch({type: CREATE_USER_SUCCESS, payload: new_user});
			Actions.LoginScreen();
		})
		.catch(error => {
			dispatch({type: CREATE_USER_FAIL});
			console.log(error);
		});
		// new Promise(function(resolve, reject) {
		// 	ncentSDKInstance.initNCNT();
		// })
		// .then( () => {
	 // 		dispatch({type: CREATE_USER_SUCCESS, payload: new_user});
		// 	Actions.LoginScreen();
		// })
		// .catch(error => {
		// 	dispatch({type: CREATE_USER_FAIL});
		// 	console.log(error);
		// });
	};
};
