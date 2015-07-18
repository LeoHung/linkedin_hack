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

func getMockMapData() -> [MapData] {
    var dataList:[MapData] = []
    var lats:[Double] = [37.425573169, 37.4587570421, 37.4631503089, 37.4563102904, 37.4661436654]
    var lngs:[Double] = [-121.9981763898, -121.9859350066, -121.9884520557, -122.0150058779, -121.9847037757]
    var titles:[NSString] = ["Pokemon nearby!", "Jeff Weiner nearby!", "HR contact nearby!", "Free food nearby!", "Taylor Swift nearby!"]
    var messages:[NSString] = ["Someone hide a pokeman nearby", "Autograph from Jeff Weiner nearby", "LinkedIn HR contact email nearby", "A truck loaded with free food nearby", "Catch up with Taylor nearby"]
    
    for i in 0...4 {
        var lat:Double = lats[i]
        var lng:Double = lngs[i]
        var title:NSString = titles[i]
        var message:NSString = messages[i]
        dataList.append(MapData(title: title, message:message, lng:lng, lat:lat))
    }

    return dataList
}

func getMockGeotifications() -> [Geotification] {
    var mapData:[MapData] = getMockMapData()
    var output:[Geotification] = []
    
    for i in 0...mapData.count-1 {
        var coordinates = CLLocationCoordinate2D(latitude: mapData[i].lat as
            CLLocationDegrees, longitude: mapData[i].lng as CLLocationDegrees)
        
        output.append(Geotification(coordinate: coordinates, radius: 5 as CLLocationDistance, identifier: mapData[i].title as String, note: mapData[i].message as String))
    }
    return output
}
