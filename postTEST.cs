using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.Networking;

// Use this script to test code. Remember to save working code
public class Test : MonoBehaviour
{
    // Define Variables
    public Vector3 cameraPos;
    public string serveraddr = "http://localhost:8000/main/";

    // Start is called before the first frame update
    void Start()
    {
        Testing();
        CameraPos();
        //StartCoroutine(PostRequest(serveraddr));
        StartCoroutine(GetRequest(serveraddr));
    }

    // Update is called once per frame
    void Update()
    {

    }

    // Define Functions
    void Testing()
    {
        Debug.Log("Testing...");
    }

    void CameraPos()
    {
        cameraPos = Camera.main.gameObject.transform.position;
        Debug.Log(cameraPos.ToString());
    }

    IEnumerator PostRequest(string url)
    {
        WWWForm form = new WWWForm();
        form.AddField("Camera Position", cameraPos.ToString());

        UnityWebRequest uwr = UnityWebRequest.Post(url, form);
        yield return uwr.SendWebRequest();

        if (uwr.isNetworkError)
        {
            Debug.Log("Error While Sending: " + uwr.error);
        }
        else
        {
            Debug.Log("Received: " + uwr.downloadHandler.text);
        }
    }

    IEnumerator GetRequest(string url)
    {
        using (UnityWebRequest webRequest = UnityWebRequest.Get(url))
        {
            // Request and wait for the desired page.
            yield return webRequest.SendWebRequest();

            string[] pages = url.Split('/');
            int page = pages.Length - 1;

            if (webRequest.isNetworkError)
            {
                Debug.Log(pages[page] + ": Error: " + webRequest.error);
            }
            else
            {
                Debug.Log(pages[page] + ":\nReceived: " + webRequest.downloadHandler.text);
            }
        }
    }
}




