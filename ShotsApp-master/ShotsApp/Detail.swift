//
//  Detail.swift
//  ShotsApp
//
//  Created by Yogesh Nagarur on 2014-08-05.
//  Copyright (c) 2014 Yogesh Nagarur. All rights reserved.
//

import UIKit

class Detail: UIViewController, UIImagePickerControllerDelegate, UINavigationControllerDelegate {
    
    @IBOutlet weak var backButton: UIButton!
    @IBOutlet weak var descriptionTextView: UITextView!
    @IBOutlet weak var imageView: UIImageView!
    @IBOutlet weak var authorLabel: UILabel!
    @IBOutlet weak var avatarImageView: UIImageView!
    
    var data = Array<Dictionary<String,String>>()
    var messageArray = Array<Dictionary<String,String>>()
    var number = 0
    var titleText: String = ""
    var imageTest: UIImage?
    
    @IBAction func backButtonDidPress(sender: AnyObject) {
        performSegueWithIdentifier("detailToHome", sender: sender)
    }
    
    override func prepareForSegue(segue: UIStoryboardSegue, sender: AnyObject!) {
        if segue.identifier == "detailToHome" {
            let controller = segue.destinationViewController as! StartController
            //controller.data = data
            //controller.number = number
            //controller.isReturned = true
            //controller.photo = imageTest
            //controller.content = descriptionTextView.text
        }
    }
    
    
    ///////////////////////////
    // Init
    //////////////////////////
    override func viewDidLoad() {
        super.viewDidLoad()
        
        authorLabel.text = data[number]["author"]
        avatarImageView.image = UIImage(named: data[number]["avatar"]!)
        imageView.image = UIImage(named: data[number]["image"]!)
        descriptionTextView.text = data[number]["text"]
        
        backButton.alpha = 0
        
        textViewWithFont(descriptionTextView, "Libertad", 16, 7)
        imageView.userInteractionEnabled = true
        imageTest = imageView.image
    }
    
    override func viewDidAppear(animated: Bool) {
        super.viewDidAppear(true)
        
        backButton.alpha = 1
        springScaleFrom(backButton!, -100, 0, 0.5, 0.5)
    }
    
    override func prefersStatusBarHidden() -> Bool  {
        return true
    }
    
    ///////////////////////////////////////////
    // Image
    ///////////////////////////////////////////
    func imagePickerControllerDidCancel(picker: UIImagePickerController) {
        dismissViewControllerAnimated(true, completion: nil)
    }
    
    func imagePickerController(picker: UIImagePickerController, didFinishPickingMediaWithInfo info: [NSObject : AnyObject]) {
        let selectedImage = info[UIImagePickerControllerOriginalImage] as! UIImage
        
        imageTest = selectedImage
        imageView.image = selectedImage
        
        dismissViewControllerAnimated(true, completion: nil)
    }
    
    @IBAction func setImage(sender: UIPanGestureRecognizer) {
        
        if sender.state == UIGestureRecognizerState.Ended {
            let imagePickerController = UIImagePickerController()
            
            let translation = sender.translationInView(view)
            
            if translation.y > 50 {
                imagePickerController.sourceType = UIImagePickerControllerSourceType.PhotoLibrary
                
                imagePickerController.delegate = self
            } else if translation.y < -50 {
                imagePickerController.sourceType = UIImagePickerControllerSourceType.Camera
                
                imagePickerController.delegate = self
            }
            
            presentViewController(imagePickerController, animated: true, completion: nil)
        }
    }
    
}
