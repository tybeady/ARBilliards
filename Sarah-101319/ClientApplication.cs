using System.Collections;
using UnityEngine;
using UnityEngine.Networking;
using System.Net;

public class ClientApplication : MonoBehaviour
{
    string serveraddr = "http://localhost:8000/billiards_main/";

    string testimage = @"C:\Users\Sarah Medved\Pictures\TSB.jpg";
    static string form_field = ""; //must be static
    static string form_data = "points";

    void Start()
    {
        Debug.Log("Connecting To Server: " + serveraddr);
    }

    public void Update()
    {
        string formfield = UnityWebRequest.EscapeURL(form_field.ToString());
        string formdata = UnityWebRequest.EscapeURL(form_data.ToString());

        //PostImage(serveraddr);
        StartCoroutine(PostRequest(serveraddr, formfield, formdata));
        //StartCoroutine(GetRequest(serveraddr));
    }

    public IEnumerator PostRequest(string url, string field, string data)
    {
        WWWForm form = new WWWForm();
        form.AddField(field, data);

        UnityWebRequest uwr = UnityWebRequest.Post(url, form);
        yield return uwr.SendWebRequest();

        if (uwr.isNetworkError)
        {
            Debug.LogError("POST REQUEST Error: " + uwr.error);
        }
        else
        {
            Debug.Log("POST REQUEST Sent!");
        }
    }

    public IEnumerator GetRequest(string url)
    {
        UnityWebRequest uwr = UnityWebRequest.Get(url);
        yield return uwr.SendWebRequest();

        string[] pages = url.Split('/');
        int page = pages.Length - 1;

        if (uwr.isNetworkError)
        {
            Debug.LogError("GET REQUEST Error: " + uwr.error);
            
        }
        else
        {
            Debug.Log("GET REQUEST Sent!");
        }
    }

    public void PostImage(string url)
    {
        using (WebClient client = new WebClient())
        {
            client.UploadFile(url, testimage);
        }
        Debug.Log("IMAGE Sent!");
    }
}