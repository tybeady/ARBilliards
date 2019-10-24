using UnityEngine;
using System.Linq;

//Takes image with HOLOLENS WEB CAMERA and saves it to desktop file (09/30/19)
public class ImageCapture : MonoBehaviour
{
    public string imgpath = "C:/Users/Sarah Medved/Desktop/Tests/Images";
    UnityEngine.Windows.WebCam.PhotoCapture photoCaptureObject = null;

    void Start()
    {
        UnityEngine.Windows.WebCam.PhotoCapture.CreateAsync(false, OnPhotoCaptureCreated);
    }

    void OnPhotoCaptureCreated(UnityEngine.Windows.WebCam.PhotoCapture captureObject)
    {
        photoCaptureObject = captureObject;

        Resolution cameraResolution = UnityEngine.Windows.WebCam.PhotoCapture.SupportedResolutions.OrderByDescending((res) => res.width * res.height).First();

        UnityEngine.Windows.WebCam.CameraParameters c = new UnityEngine.Windows.WebCam.CameraParameters();
        c.hologramOpacity = 0.0f;
        c.cameraResolutionWidth = cameraResolution.width;
        c.cameraResolutionHeight = cameraResolution.height;
        c.pixelFormat = UnityEngine.Windows.WebCam.CapturePixelFormat.BGRA32;

        captureObject.StartPhotoModeAsync(c, OnPhotoModeStarted);
    }

    private void OnPhotoModeStarted(UnityEngine.Windows.WebCam.PhotoCapture.PhotoCaptureResult result)
    {
        if (result.success)
        {
            string filename = string.Format(@"CapturedImage{0}_n.jpg", Time.time);
            string filePath = System.IO.Path.Combine(imgpath, filename);
            photoCaptureObject.TakePhotoAsync(filePath, UnityEngine.Windows.WebCam.PhotoCaptureFileOutputFormat.JPG, OnCapturedPhotoToDisk);
        }
        else
        {
            Debug.LogError("IMAGE CAPTURE Error: Unable to start photo mode");
        }
    }

    void OnCapturedPhotoToDisk(UnityEngine.Windows.WebCam.PhotoCapture.PhotoCaptureResult result)
    {
        if (result.success)
        {
            Debug.Log("IMAGE CAPTURE Success!");
            photoCaptureObject.StopPhotoModeAsync(OnStoppedPhotoMode);
        }
        else
        {
            Debug.LogError("IMAGE CAPTURE Error: Unable to capture image");
        }
    }

    void OnStoppedPhotoMode(UnityEngine.Windows.WebCam.PhotoCapture.PhotoCaptureResult result)
    {
        photoCaptureObject.Dispose();
        photoCaptureObject = null;
    }

}