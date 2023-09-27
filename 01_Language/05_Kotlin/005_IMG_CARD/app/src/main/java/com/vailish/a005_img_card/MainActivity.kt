package com.vailish.a005_img_card

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.compose.foundation.Image
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.Favorite
import androidx.compose.material.icons.filled.FavoriteBorder
import androidx.compose.material3.Card
import androidx.compose.material3.CardDefaults
import androidx.compose.material3.Icon
import androidx.compose.material3.IconButton
import androidx.compose.runtime.Composable
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.runtime.getValue
import androidx.compose.runtime.saveable.rememberSaveable
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.layout.ContentScale
import androidx.compose.ui.res.painterResource
import androidx.compose.ui.unit.dp

class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContent {
//            ImageCard()
//            ImageCard2()
            // 3번쓸때만 필요
            var isFavorite by rememberSaveable {
                mutableStateOf(false)
            }
            ImageCard3(
                Modifier.fillMaxWidth(0.5f)
                .padding(16.dp),
                isFavorite = isFavorite,
            ) {
                favorite ->
                isFavorite = favorite
            }
        }
    }
}


@Composable
fun ImageCard3(
    modifier: Modifier = Modifier,
    isFavorite: Boolean,
    onTabFavorite: (Boolean) -> Unit,
) {

    Card(
        modifier = modifier,
        shape = RoundedCornerShape(8.dp),
        elevation = CardDefaults.cardElevation(5.dp),
    ) {
        Box(
            modifier = Modifier.height(200.dp),
        ) {
            Image(
                painter = painterResource(id = R.drawable.img),
                contentDescription = "cat",
                contentScale = ContentScale.Crop,
            )
            Box(
                modifier = Modifier.fillMaxSize(),
                contentAlignment = Alignment.TopEnd,
            ) {
                IconButton(onClick = {
                    onTabFavorite(!isFavorite) // .invoke 생략가능
                }) {
                    Icon(
                        imageVector = if (isFavorite) Icons.Default.Favorite else Icons.Default.FavoriteBorder,
                        contentDescription = "favorite",
                        tint = Color.Black,
                    )
                }
            }
        }
    }
}

//
//@Composable
//fun ImageCard() {
//    var isFavorite = remember {
//        mutableStateOf(false)
//    }
//
//    Card(
//        modifier = Modifier
//            .fillMaxWidth(0.5f)
//            .padding(16.dp),
//        shape = RoundedCornerShape(8.dp),
//        elevation = CardDefaults.cardElevation(5.dp),
//    ) {
//        Box(
//            modifier = Modifier.height(200.dp),
//        ) {
//            Image(
//                painter = painterResource(id = R.drawable.img),
//                contentDescription = "cat",
//                contentScale = ContentScale.Crop,
//            )
//            Box(
//                modifier = Modifier.fillMaxSize(),
//                contentAlignment = Alignment.TopEnd,
//            ) {
//                IconButton(onClick = {
//                    isFavorite.value = !isFavorite.value
//                }) {
//                    Icon(
//                        imageVector = if (isFavorite.value) Icons.Default.Favorite else Icons.Default.FavoriteBorder,
//                        contentDescription = "favorite",
//                        tint = Color.Black,
//                    )
//                }
//            }
//        }
//    }
//}

//@Composable
//fun ImageCard2() {
//    var isFavorite by rememberSaveable {
//        mutableStateOf(false)
//    }
//
//    Card(
//        modifier = Modifier
//            .fillMaxWidth(0.5f)
//            .padding(16.dp),
//        shape = RoundedCornerShape(8.dp),
//        elevation = CardDefaults.cardElevation(5.dp),
//    ) {
//        Box(
//            modifier = Modifier.height(200.dp),
//        ) {
//            Image(
//                painter = painterResource(id = R.drawable.img),
//                contentDescription = "cat",
//                contentScale = ContentScale.Crop,
//            )
//            Box(
//                modifier = Modifier.fillMaxSize(),
//                contentAlignment = Alignment.TopEnd,
//            ) {
//                IconButton(onClick = {
//                    isFavorite = !isFavorite
//                }) {
//                    Icon(
//                        imageVector = if (isFavorite) Icons.Default.Favorite else Icons.Default.FavoriteBorder,
//                        contentDescription = "favorite",
//                        tint = Color.Black,
//                    )
//                }
//            }
//        }
//    }
//}

