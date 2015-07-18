//
//  Utilities.swift
//  Geotify
//
//  Created by Ken Toh on 3/3/15.
//  Copyright (c) 2015 Ken Toh. All rights reserved.
//

import UIKit
import MapKit

// MARK: Helper Functions

func showSimpleAlertWithTitle(title: String!, #message: String, #viewController: UIViewController) {
  let alert = UIAlertController(title: title, message: message, preferredStyle: .Alert)
  let action = UIAlertAction(title: "OK", style: .Cancel, handler: nil)
  alert.addAction(action)
  viewController.presentViewController(alert, animated: true, completion: nil)
}

func zoomToUserLocationInMapView(mapView: MKMapView) {
  if let coordinate = mapView.userLocation.location?.coordinate {
    let region = MKCoordinateRegionMakeWithDistance(coordinate, 10000, 10000)
    mapView.setRegion(region, animated: true)
  }
}

func getMockCardData() -> [MapData] {
    var dataList:[MapData] = []
    
    for i in 0..4 {
        
    }
    
    
    for i in 0...7 {
        var contact:Contact = contacts[i]
        var message:NSString = messages[i]
        var monthDate:NSString = "Aug 30"
        var year:NSString = "2013"
        var sender = contact.name
        var imageName:String = "TestImg" + String(i) + ".JPG"
        var photo:UIImage = UIImage(named:imageName)!
        
        contact.name = "Jack Liao"
        dataList.append(CardData(contact: contact, message: message, monthDate: monthDate, year: year, sender: sender, photo: photo))
    }
    return dataList
}
